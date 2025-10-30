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

  long double left = 0, right = 100; // диапазон p, %
  const long double eps = 1e-7;

  // проверка на p = 0
  if (fabsl(s - m * 12 * n) < 1e-12) {
    cout.setf(ios::fixed);
    cout.precision(6);
    cout << 0.0L << endl;
    return 0;
  }

  // если платеж слишком мал, решения при p >= 0 нет
  if (m < s / (12.0L * n) - 1e-12) {
    cout << "Решения при p >= 0 нет (слишком маленький платеж)" << endl;
    return 0;
  }

  while (right - left >= eps) {
    p = (left + right) / 2;
    r = p / 100; // годовая доля
    long double temp = pow(1 + r, n);

    calc = (s * r * temp) / (12 * (temp - 1)); // платеж по формуле из задания

    if (calc > m)
      right = p;
    else
      left = p; // включаем равенство, чтобы не зациклиться
  }

  cout.setf(ios::fixed);
  cout.precision(6);
  cout << (left + right) / 2 << endl; // выводим p в % годовых

  return 0;
}
