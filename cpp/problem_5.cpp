#include <iostream>
using namespace std;

int main() {
  long long N, K;
  cout << "Введите N и K: ";
  cin >> N >> K;
  if (K > N) {
    cout << "K не может быть больше N!" << endl;
    return 1;
  }
  if (K <= 0 || N <= 0) {
    cout << "Отрицательное значение!" << endl;
    return 1;
  }
  while (K != 1) {
    N = (N - K % 2) / 2;
    K = K / 2;
  }

  long long left = (N - 1) / 2;
  long long right = N / 2;

  // неубывание
  if (left > right)
    swap(left, right);

  cout << "Левый купе: " << left << endl;
  cout << "Правый купе: " << right << endl;

  return 0;
}
