#include <cmath>
#include <iostream>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №2" << endl;
  cout
      << R"(Условие: Для произвольных x, y, b вычислить функцию z = ln(b-y) * корень(b-x))"
      << endl;

  float x, y, b;
  cout << "Введите x, y, b: ";
  cin >> x >> y >> b;
  if (b <= y)
    cout << "Нет решений";
  else if (b < x)
    cout << "Нет решений";
  else
    cout << log(b - y) * sqrt(b - x) + 0 << endl;

  return 0;
}
