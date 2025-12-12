#include <cmath>
#include <iostream>
#include <string>
using namespace std;

void sum_of_sin() {
  cout << endl
       << R"(1) Дано целое число n (вводится с клавиатуры).
Вычислить: y = 1 / sin(1) + 2 / (sin(1) + sin(2)) + 3 / (sin(1) + sin(2) + sin(3)) + ... + n / (sin(1) + sin(2) + ... + sin(n)))"
       << endl;
  cout << string(50, '-') << endl;
  int n;
  cout << "Введите n: ";
  cin >> n;
  if (n < 0) {
    cout << "Отрицательное значение" << endl;
    return;
  }

  double sum = 0.0;
  double sum_sin = 0.0;
  for (int i = 1; i <= n; i++) {
    sum_sin += sin(i);
    if (fabs(sum_sin) < 1e-10) {
      cout << "Деление на ноль";
      return;
    }
    sum += i / sum_sin;
  }
  cout << "y = " << sum << endl;
}

void third_word() {
  cout << endl
       << "26) Дана строка S из n символов, в которой символом «пробел» "
          "разделяются слова. Вывести на экран третье слово в обратном порядке"
       << endl;
  cout << string(50, '-') << endl;
  int n;
  cout << "Введите n: ";
  cin >> n;
  if (n < 0) {
    cout << "Отрицательное значение" << endl;
    return;
  }
  string s;
  cout << "Введите строку s: ";
  cin.ignore(); // очистка буфера
  getline(cin, s);
  if (s.size() != n) {
    cout << "Строка не из n символов" << endl;
    return;
  }
  s += ' '; //  обработки последнего слова

  string word[3];
  int index = 0;
  bool in_word = false;
  for (int i = 0; i < s.size() && index < 3; i++) {
    if (s[i] != ' ') {
      in_word = true;
      word[index] += s[i];
    } else {
      if (in_word) {
        index++;
        in_word = false;
      }
    }
  }

  if (index < 3) {
    cout << "Слов меньше трёх" << endl;
    return;
  }

  cout << "Третье слово в обратном порядке: ";
  for (int i = word[2].size() - 1; i >= 0; i--) {
    cout << word[2][i];
  }
  cout << endl;
}

void matrix() {
  cout << endl
       << "51) Написать программу, которая вводит по строкам с клавиатуры "
          "двумерный массив и вычисляет сумму его элементов в четных столбцах"
       << endl;
  cout << string(50, '-') << endl;
  int n, m;
  cout << "Введите количество строк, столбцов" << endl
       << "(недописанные элементы приравниваются к 0, лишние элементы "
          "отбрасываются): ";
  cin >> n >> m;
  cin.ignore(); // иначе первая строка = '\n'

  double matrix[n][m];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++)
      matrix[i][j] = 0;
  }

  string s;
  cout << "Введите матрицу:" << endl;

  for (int i = 0; i < n; i++) {
    int j = 0;
    getline(cin, s);
    s += ' '; // для обработки последнего числа
    string N = "";
    for (char c : s) {
      if (c != ' ') {
        N += c;
      } else {
        if (!N.empty() && j < m) {
          matrix[i][j++] = stod(N);
          N = "";
        }
      }
    }
  }

  double sum = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 1; j < m; j += 2) {
      sum += matrix[i][j];
    }
  }
  cout << "Сумма элементов четных столбцов: " << sum << endl;
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №5" << endl;
  cout << R"(Условие: Выполнить три варианта задания)" << endl;
  cout << string(50, '=') << endl;
  sum_of_sin();
  third_word();
  matrix();
}
