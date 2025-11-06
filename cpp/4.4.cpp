#include <iostream>
using namespace std;

void generator(long long m, long long i, long long c, long long k) {
  long long s[i + 1];
  s[0] = 0;
  for (long long j = 0; j < i; j++) {
    s[j + 1] = (m * s[j] + j) % c;
  }
  cout << "Первые " << k + 1 << " чисел: ";
  for (int j = 0; j < k + 1; j++) {
    cout << s[j] << ' ';
  }
  cout << endl;
}

int main() {
  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout << R"(Условие: Построить генератор
псевдослучайных чисел по рекуррентной формуле:
s_{i+1} = (m*s_i + i) mod c, где m, i, c – целые числа.)"
       << endl;
  generator(37, 3, 64, 3);
  generator(25173, 13849, 65537, 11);
}
