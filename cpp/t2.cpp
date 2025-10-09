#include <algorithm>
#include <codecvt> // да, deprecated, но в g++ работает
#include <fstream>
#include <iostream>
#include <locale>
#include <string>

using namespace std;

int main() {
  ios::sync_with_stdio(false);

  // Терминал у тебя UTF-8, заставим wide-потоки тоже быть UTF-8
  locale utf8_locale(locale(), new codecvt_utf8<wchar_t>);
  wcout.imbue(utf8_locale);

  wcout << L"КВБО-11-25 Шапаренко Фёдор Александрович\n";
  wcout << L"Практическое задание №2\n";

  wifstream fin("30.txt", ios::binary);
  fin.imbue(utf8_locale);

  wstring s;
  getline(fin, s);

  if (s.length() > 30) {
    wcout << L"Файл состоит из больше чем 30 букв\n";
  } else {
    sort(s.begin(), s.end());
    wcout << L"Результат: " << s << L"\n";
  }
}
