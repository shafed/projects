#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void ascii() {
  cout << endl << "8. Преобразование текста в цепочку ASCII-кодов" << endl;
  cout << string(50, '-') << endl;

  ifstream fin("text.txt");
  if (!fin.is_open()) {
    cout << "Error 1";
    return;
  }

  string line;
  int n = 1;
  while (getline(fin, line)) {
    cout << "Строка " << n++ << ": ";
    for (char c : line) {
      cout << int(c) << " ";
    }
    cout << endl;
  }
  fin.close();
}

void entrance() {
  cout << endl
       << "39. Подсчет числа вхождений символов в текстовый файл" << endl;
  cout << string(50, '-') << endl;

  int cnt[256] = {0};

  ifstream fin("text.txt");
  if (!fin.is_open()) {
    cout << "Error 1";
    return;
  }

  string line;
  while (getline(fin, line)) {
    for (char c : line) {
      cnt[int(c)] += 1;
    }
  }

  // symbols
  for (int i = 0; i < 256; i++) {
    if (cnt[i] != 0)
      cout << char(i) << " ";
  }

  cout << endl;

  // cnt
  for (int i = 0; i < 256; i++) {
    if (cnt[i] != 0)
      cout << cnt[i] << " ";
  }
  fin.close();
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №5" << endl;
  cout << R"(Условие: Выполнить два варианта задания)" << endl;

  ofstream fout("text.txt");
  if (!fout.is_open()) {
    cout << "Error 1";
    return 1;
  }

  fout << "Hello world;" << endl;
  fout << "I'm good." << endl;
  fout.close();

  ifstream fin("text.txt");
  if (!fin.is_open()) {
    cout << "Error 1";
    exit(1);
  }

  cout << string(50, '=') << endl;
  string line;
  while (getline(fin, line)) {
    cout << line << endl;
  }
  fin.close();
  cout << string(50, '=') << endl;

  ascii();
  cout << endl;
  entrance();
}
