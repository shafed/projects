#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void m(int a, int b) {
  while (a != 0 && b != 0) {
    if (a > b) {
      a = a % b;
    } else {
      b = b % a;
    }
  }
  cout << a + b;
}

void d(int a, int b) {
  while (a != 0 && b != 0) {
    if (a > b) {
      a
    }
  }
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №3" << endl;
  cout << R"(Условие: Задать 2 числа и найти их наибольший
общий делитель двумя способами: делением и вычитанием.)"
       << endl;

  int a, b;
  cout << "Введите числа a, b: " << endl;
  cin >> a >> b;
  m(a, b);

  return 0;
}
