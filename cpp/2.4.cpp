#include <cmath>
#include <iomanip>
#include <iostream>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №2" << endl;
  cout
      << R"(Условие: Протабулируйте функцию y = (x*x - 2*x + 2)/(x-1) при изменение x от -4 до +4 с шагом 0.5)"
      << endl;
  float x, y;
  cout << setw(10) << left << "x" << setw(15) << left << "y" << endl;

  for (x = -4; x <= 4; x += 0.5)
    if (x != 1) {
      y = (x * x - 2 * x + 2) / (x - 1);
      cout << setw(10) << left << fixed << setprecision(2) << x << setw(15)
           << left << fixed << setprecision(2) << y << endl;
    } else
      cout << setw(10) << x << setw(30) << "y не определен" << endl;
  return 0;
}
