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

  long double left = 0, right = 10000;
  if (s == m * 12 * n)
    cout << 0;
  else {
    while (left - right >= 1e-6) {

      p = (left + right) / 2;
      r = p / 100;
      double temp = pow(1 + r, n);

      calc = (s * r * temp) / (12 * (temp - 1));
      if (calc > m)
        right = p;
      else if (calc < m)
        left = p;
      else {
        cout << p;
        break;
      }
    }
  }

  return 0;
}
