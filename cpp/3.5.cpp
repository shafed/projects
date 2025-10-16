#include <iostream>
#include <vector>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №3" << endl;
  cout << R"(Условие: Найти все простые числа в диапазоне от 2
до введенного вами натурального числа.)"
       << endl;

  int n, i = 2, j;
  cout << "Введите натуральное число: ";
  cin >> n;
  vector<int> primes;
  for (int k = 0; k <= n; k++) {
    primes.push_back(k);
  }

  if (n < 1) {
    cout << "Введено не натуральное число" << endl;
    return 1;
  }
  if (n == 1) {
    cout << "1 не простое число" << endl;
    return 1;
  }

  while (i < n) {
    if (primes[i] != 0) {
      j = i * 2;
      while (j <= n) {
        primes[j] = 0;
        j = j + i;
      }
    }
    i++;
  }
  for (auto k : primes) {
    if (k >= 2) {
      cout << k << " ";
    }
  }

  return 0;
}
