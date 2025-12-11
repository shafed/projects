#include <iostream>
using namespace std;

int main() {

  long long a, b, c;
  cout << "Введите A, B, C: ";
 cin >> a >> b >> c;

  if (a <= 0 || b <= 0 || c <= 0) {
    cout << "Отрицательное значение!";
    return 0;
  }

  if (a > c) {
    cout << "Цена товара превышает максимальную!";
    return 1;
  }

  cout << "Максимальное количество лопастей: " << (c - a) / b;
  return 0;
}
