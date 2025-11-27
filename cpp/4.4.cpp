#include <iostream>
using namespace std;
typedef long long ll;

ll s(ll m, ll i, ll c) {
  if (i == 0)
    return 0;
  return (m * s(m, i - 1, c) + i) % c;
}

int main() {
  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout << R"(Условие: Построить генератор
псевдослучайных чисел по рекуррентной формуле:
s_{i+1} = (m*s_i + i) mod c, где m, i, c – целые числа.)"
       << endl;
  ll a, b;
  a = s(37, 3, 64);
  b = s(25173, 13849, 65537);
  cout << a << endl;
  cout << b << endl;
}
