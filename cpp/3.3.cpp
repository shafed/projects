#include <algorithm>
#include <codecvt>
#include <fstream>
#include <iostream>
#include <locale>
#include <string>
using namespace std;

int main() {
  locale::global(locale("ru_RU.UTF-8"));

  wcout << L"КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  wcout << L"Практическое задание №3" << endl;
  wcout << L"Условие: Задать строку из 30 букв и расставить их в алфавитном "
           L"порядке"
        << endl;
  wstring f;
  wcout << L"Введите строку: ";
  wcin >> f;
  wofstream fout("30.txt");
  if (!fout.is_open()) {
    wcout << L"Не удалось открыть файл" << endl;
    return 1;
  } else {
    fout << f;
    fout.close();
  }

  wifstream fin("30.txt");

  if (!fin.is_open()) {
    wcout << L"Не удалось открыть файл" << endl;
    return 1;
  }

  wstring s;
  getline(fin, s);
  fin.close();

  for (wchar_t c : s) {
    if (!iswalpha(c)) {
      wcout << L"В файле есть не буквы: ";
      for (wchar_t d : s)
        if (!iswalpha(d)) {
          wcout << d;
        }
      return 1;
    }
  }

  if (s.length() > 30) {
    wcout << L"Файл состоит из больше чем 30 букв: " << s.length() << endl;
    return 1;
  }

  sort(s.begin(), s.end());
  wcout << L"Строка: " << s << endl;
  return 0;
}
