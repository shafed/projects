#include <iostream>
using namespace std;

void m(int a, int b) {
  while (a != 0 && b != 0) {
    if (a > b) {
      a = a % b;
    } else {
      b = b % a;
    }
  }
  cout << "Деление: " << a + b << endl;
}

void d(int a, int b) {
  if (a == 0 || b == 0) {
    cout << "Разность: " << a + b << endl;
  } else {
    while (a != b) {
      if (a > b) {
        a = a - b;
      } else {
        b = b - a;
      }
    }
    cout << "Разность: " << a << endl;
  }
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №3" << endl;
  cout << R"(Условие: Задать 2 числа и найти их наибольший
общий делитель двумя способами: делением и вычитанием.)"
       << endl;

  int a, b;
  cout << "Введите числа a, b: ";
  cin >> a >> b;

  if (a == 0 && b == 0) {
    cout << "НОД(0, 0) не определен";
    return 1;
  }

  a = abs(a);
  b = abs(b);

  m(a, b);
  d(a, b);
  return 0;
}
