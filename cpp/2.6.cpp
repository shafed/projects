#include <cmath>
#include <iostream>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №2" << endl;
  cout
      << R"(Условие: Под какой процент p выдана ссуда величиной S рублей, которая гасится месячными выплатами величиной m в течение n лет.
 Формула:
 m = (Sr * (1+r)^n) / (12 * ((1+r)^n - 1)), где r = p/100)"
      << endl;

  long double m, s, n, p, r, calc;
  cout << "Введите S, m, n: ";
  cin >> s >> m >> n;
  if (s <= 0 || m <= 0 || n <= 0) {
    cout << "Отрицательные значения" << endl;
    return 1;
  }

  if ((m - s / (12 * n)) < -1e-9) {
    cout << "Платёж слишком мал" << endl;
    return 1;
  }

  long double left = 0, right = 100;
  if (fabs(s - m * 12 * n) < 1e-9) {
    cout << 0;
    return 0;
  }

  while (right - left >= 1e-7) {
    p = (left + right) / 2;
    r = p / 100;
    long double temp = pow(1 + r, n);

    calc = (s * r * temp) / (12 * (temp - 1));
    if (calc > m)
      right = p;
    else
      left = p;
  }
  cout << (left + right) / 2;

  return 0;
}
