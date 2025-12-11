#include <iostream>
using namespace std;

int main() {
  int N;
  cout << "Введите N: ";
  cin >> N;
  if (N < 0) {
    cout << "Отрицательное значение!" << endl;
    return 1;
  }

  int free[9] = {0};

  for (int i = 0; i < N; ++i) {
    int seat;
    cout << "Введите место: ";
    cin >> seat;
    if (seat < 0) {
      cout << "Отрицательное значение!" << endl;
      return 1;
    }

    int index;
    if (1 <= seat && seat <= 36) {
      index = (seat - 1) / 4;
    } else if (37 <= seat && seat <= 54) {
      index = 9 - (seat - 37) / 2 - 1;
    }

    if (index >= 0 && index < 9) {
      free[index]++;
    }
  }

  int best = 0;
  int curr = 0;
  for (int i = 0; i < 9; ++i) {
    if (free[i] == 6) {
      curr++;
      best = max(best, curr);
    } else {
      curr = 0;
    }
  }

  cout << "Максимальное количество свободных мест: " << best;
  return 0;
}
