"""Tkinter GUI: выбор файлов, таблица, экспорт, штрихкоды."""

from __future__ import annotations

import logging
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, ttk
from passport_mvp.config.settings import DEFAULT_SETTINGS, AppSettings
from passport_mvp.models.record import PassportRecord
from passport_mvp.services import barcode_gen, export, file_loader, pipeline
from passport_mvp.services.normalization import normalize_record
from passport_mvp.utils.logging_setup import setup_logging

logger = logging.getLogger(__name__)


class MainWindow:
    """Главное окно приложения (логика вынесена из виджетов в методы класса)."""

    def __init__(self, root: tk.Tk, settings: AppSettings = DEFAULT_SETTINGS) -> None:
        self.root = root
        self.settings = settings
        self._files: list[Path] = []
        self._records: list[PassportRecord] = []

        root.title("Оцифровка паспортов оборудования — MVP")
        root.geometry("1280x760")
        root.minsize(980, 620)

        self._build_layout()

    def _build_layout(self) -> None:
        pad = {"padx": 8, "pady": 6}

        top = ttk.Frame(self.root)
        top.pack(fill=tk.X, **pad)

        ttk.Button(top, text="Выбрать файлы…", command=self._on_pick_files).pack(side=tk.LEFT, padx=4)
        ttk.Button(top, text="Выбрать папку…", command=self._on_pick_folder).pack(side=tk.LEFT, padx=4)
        ttk.Button(top, text="Запустить обработку", command=self._on_process).pack(side=tk.LEFT, padx=4)

        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=4)

        mid = ttk.Frame(self.root)
        mid.pack(fill=tk.BOTH, expand=True, **pad)

        left = ttk.Frame(mid)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        cols = PassportRecord.export_columns()
        self._tree = ttk.Treeview(left, columns=cols, show="headings", selectmode="browse")
        for c in cols:
            self._tree.heading(c, text=c)
            self._tree.column(c, width=120, stretch=True)

        vsb = ttk.Scrollbar(left, orient="vertical", command=self._tree.yview)
        hsb = ttk.Scrollbar(left, orient="horizontal", command=self._tree.xview)
        self._tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self._tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        left.grid_rowconfigure(0, weight=1)
        left.grid_columnconfigure(0, weight=1)

        self._tree.bind("<Double-1>", self._on_cell_double_click)

        right = ttk.Frame(mid, width=360)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

        ttk.Label(right, text="Статус обработки").pack(anchor="w")
        self._status = tk.StringVar(value="Готово.")
        ttk.Label(right, textvariable=self._status, wraplength=330).pack(anchor="w")

        ttk.Separator(right, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=8)

        ttk.Label(right, text="Сводка").pack(anchor="w")
        self._summary = tk.StringVar(value="Файлов: 0 | Строк: 0")
        ttk.Label(right, textvariable=self._summary, wraplength=330).pack(anchor="w")

        ttk.Label(right, text="Ошибки файлов").pack(anchor="w", pady=(8, 0))
        self._errors = tk.Listbox(right, height=6, exportselection=False)
        self._errors.pack(fill=tk.BOTH, expand=False)

        ttk.Separator(right, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=8)

        ttk.Label(right, text="Штрихкоды (пути к PNG)").pack(anchor="w")
        self._barcodes = tk.Listbox(right, height=10, exportselection=False)
        self._barcodes.pack(fill=tk.BOTH, expand=True)

        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=4)

        bottom = ttk.Frame(self.root)
        bottom.pack(fill=tk.X, **pad)

        ttk.Label(bottom, text="cabinet_id (шкаф):").pack(side=tk.LEFT)
        self._cabinet_var = tk.StringVar(value="")
        ttk.Entry(bottom, textvariable=self._cabinet_var, width=28).pack(side=tk.LEFT, padx=6)
        ttk.Button(bottom, text="Сгенерировать штрихкод шкафа", command=self._on_cabinet_barcode).pack(
            side=tk.LEFT, padx=4
        )
        ttk.Button(bottom, text="Пересоздать штрихкоды строк", command=self._on_regen_row_barcodes).pack(
            side=tk.LEFT, padx=4
        )

        ttk.Separator(bottom, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=8)

        ttk.Button(bottom, text="Сохранить CSV…", command=self._on_save_csv).pack(side=tk.LEFT, padx=4)
        ttk.Button(bottom, text="Сохранить XLSX…", command=self._on_save_xlsx).pack(side=tk.LEFT, padx=4)

    def _set_status(self, text: str) -> None:
        self._status.set(text)
        self.root.update_idletasks()

    def _refresh_tree(self) -> None:
        self._tree.delete(*self._tree.get_children())
        for idx, r in enumerate(self._records):
            vals = [r.as_export_row()[c] for c in PassportRecord.export_columns()]
            self._tree.insert("", tk.END, iid=str(idx), values=vals)

    def _refresh_barcodes_list(self) -> None:
        self._barcodes.delete(0, tk.END)
        seen = set()
        for r in self._records:
            if r.barcode_file and r.barcode_file not in seen:
                self._barcodes.insert(tk.END, r.barcode_file)
                seen.add(r.barcode_file)
            if r.cabinet_barcode_file and r.cabinet_barcode_file not in seen:
                self._barcodes.insert(tk.END, r.cabinet_barcode_file)
                seen.add(r.cabinet_barcode_file)

    def _refresh_summary(self, files_ok: int, files_total: int, rows: int) -> None:
        self._summary.set(f"Обработано файлов (успешно): {files_ok} / {files_total} | Строк в таблице: {rows}")

    def _on_pick_files(self) -> None:
        paths = filedialog.askopenfilenames(
            title="Выберите PDF/изображения",
            filetypes=[
                ("Поддерживаемые", "*.pdf *.png *.jpg *.jpeg"),
                ("Все файлы", "*.*"),
            ],
        )
        if not paths:
            return
        self._files = [Path(p) for p in paths]
        self._set_status(f"Выбрано файлов: {len(self._files)}")

    def _on_pick_folder(self) -> None:
        d = filedialog.askdirectory(title="Выберите папку с документами")
        if not d:
            return
        self._files = file_loader.iter_files_in_directory(Path(d), recursive=False)
        self._set_status(f"Найдено файлов в папке: {len(self._files)}")

    def _on_process(self) -> None:
        if not self._files:
            messagebox.showwarning("Нет файлов", "Сначала выберите файлы или папку.")
            return

        self._set_status("Обработка… (интерфейс не зависнет)")
        threading.Thread(target=self._process_worker, daemon=True).start()

    def _process_worker(self) -> None:
        try:
            files = list(self._files)

            def prog(msg: str) -> None:
                self.root.after(0, lambda: self._set_status(msg))

            records, stats = pipeline.process_files(files, settings=self.settings, on_progress=prog)

            def done() -> None:
                self._records = records
                self._errors.delete(0, tk.END)
                for e in stats.errors:
                    self._errors.insert(tk.END, e)
                self._refresh_summary(stats.files_ok, stats.files_total, len(self._records))
                if stats.cabinet_guess and not self._cabinet_var.get().strip():
                    self._cabinet_var.set(stats.cabinet_guess)

                # Штрихкоды строк — сразу после успешного извлечения
                out_barcodes = self.settings.barcodes_dir
                barcode_gen.generate_row_barcode_files(self._records, out_barcodes)
                self._refresh_tree()
                self._refresh_barcodes_list()
                self._set_status("Готово. Проверьте таблицу и при необходимости отредактируйте ячейки.")

            self.root.after(0, done)
        except Exception as e:  # noqa: BLE001
            logger.exception("Критическая ошибка в потоке обработки")
            self.root.after(0, lambda: messagebox.showerror("Ошибка", str(e)))
            self.root.after(0, lambda: self._set_status("Ошибка обработки."))

    def _record_from_tree_values(self, idx: int, values: tuple[str, ...]) -> None:
        cols = PassportRecord.export_columns()
        data = {cols[i]: values[i] for i in range(min(len(cols), len(values)))}
        merged = {**self._records[idx].as_export_row(), **data}
        merged["internal_row_id"] = self._records[idx].internal_row_id
        rec = PassportRecord.from_mapping(merged)
        normalize_record(rec)
        self._records[idx] = rec

    def _on_cell_double_click(self, event: tk.Event) -> str | None:
        region = self._tree.identify("region", event.x, event.y)
        if region != "cell":
            return "break"

        row_id = self._tree.identify_row(event.y)
        col_id = self._tree.identify_column(event.x)
        if not row_id:
            return "break"

        idx = int(row_id)
        col_index = int(col_id.replace("#", "")) - 1
        cols = PassportRecord.export_columns()
        if col_index < 0 or col_index >= len(cols):
            return "break"

        field = cols[col_index]
        current = self._records[idx].as_export_row().get(field, "")

        dlg = tk.Toplevel(self.root)
        dlg.title("Редактирование ячейки")
        dlg.transient(self.root)
        dlg.grab_set()

        ttk.Label(dlg, text=f"Поле: {field}").pack(anchor="w", padx=10, pady=(10, 4))
        var = tk.StringVar(value=str(current))
        ent = ttk.Entry(dlg, textvariable=var, width=80)
        ent.pack(fill=tk.X, padx=10, pady=4)
        ent.focus_set()

        def ok() -> None:
            vals = list(self._tree.item(row_id, "values"))
            while len(vals) < len(cols):
                vals.append("")
            vals[col_index] = var.get()
            self._tree.item(row_id, values=vals)
            self._record_from_tree_values(idx, tuple(vals))
            dlg.destroy()

        def cancel() -> None:
            dlg.destroy()

        btns = ttk.Frame(dlg)
        btns.pack(fill=tk.X, padx=10, pady=10)
        ttk.Button(btns, text="OK", command=ok).pack(side=tk.RIGHT)
        ttk.Button(btns, text="Отмена", command=cancel).pack(side=tk.RIGHT, padx=(0, 8))
        dlg.bind("<Return>", lambda _e: ok())
        return "break"

    def _on_regen_row_barcodes(self) -> None:
        if not self._records:
            messagebox.showinfo("Нет данных", "Сначала выполните обработку.")
            return
        barcode_gen.generate_row_barcode_files(self._records, self.settings.barcodes_dir)
        self._refresh_tree()
        self._refresh_barcodes_list()
        self._set_status("Штрихкоды строк пересозданы.")

    def _on_cabinet_barcode(self) -> None:
        cid = self._cabinet_var.get().strip()
        if not cid:
            messagebox.showwarning("cabinet_id", "Введите идентификатор шкафа вручную.")
            return
        if not self._records:
            messagebox.showinfo("Нет данных", "Сначала выполните обработку.")
            return
        payload, path = barcode_gen.generate_cabinet_barcode(cid, self.settings.barcodes_dir)
        if not path:
            messagebox.showerror("Ошибка", "Не удалось создать штрихкод шкафа (см. лог).")
            return
        barcode_gen.attach_cabinet_barcode_to_rows(self._records, cid, path)
        self._refresh_tree()
        self._refresh_barcodes_list()
        self._set_status(f"Штрихкод шкафа создан: {path} (payload={payload})")

    def _on_save_csv(self) -> None:
        if not self._records:
            messagebox.showinfo("Нет данных", "Нечего сохранять.")
            return
        p = filedialog.asksaveasfilename(
            title="Сохранить CSV",
            defaultextension=".csv",
            initialfile=self.settings.results_csv_name,
            filetypes=[("CSV", "*.csv")],
        )
        if not p:
            return
        try:
            export.export_csv(self._records, Path(p))
            self._set_status(f"CSV сохранён: {p}")
        except Exception as e:  # noqa: BLE001
            messagebox.showerror("Ошибка экспорта", str(e))

    def _on_save_xlsx(self) -> None:
        if not self._records:
            messagebox.showinfo("Нет данных", "Нечего сохранять.")
            return
        p = filedialog.asksaveasfilename(
            title="Сохранить XLSX",
            defaultextension=".xlsx",
            initialfile=self.settings.results_xlsx_name,
            filetypes=[("Excel", "*.xlsx")],
        )
        if not p:
            return
        try:
            export.export_xlsx(self._records, Path(p))
            self._set_status(f"XLSX сохранён: {p}")
        except Exception as e:  # noqa: BLE001
            messagebox.showerror("Ошибка экспорта", str(e))


def run_app() -> None:
    """Точка входа GUI: логи, каталоги, главный цикл Tk."""
    settings = DEFAULT_SETTINGS
    settings.output_dir.mkdir(parents=True, exist_ok=True)
    settings.barcodes_dir.mkdir(parents=True, exist_ok=True)
    settings.logs_dir.mkdir(parents=True, exist_ok=True)
    setup_logging(settings.logs_dir)

    root = tk.Tk()
    # Чуть аккуратнее на разных темах
    try:
        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")
    except tk.TclError:
        pass

    MainWindow(root, settings=settings)
    root.mainloop()
