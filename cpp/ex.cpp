#include <iostream>
using namespace std;

int main() {
  setlocale(LC_ALL, "ru");
  long long A, B, C, N;
  cout << "Введите A: ";
  cin >> A;
  cout << "Введите B: ";
  cin >> B;
  cout << "Введите C: ";
  cin >> C;
  if (A < 0 or B < 0 or C < 0) {
    cout << "Отрицательное значение!";
  }
  if (A > C) {
    cout << "Покупатель не будет покупать товар!";
    return 1;
  }
  N = 0;
  while (A + B * N <= C) {
    N += 1;
  }
  cout << "Максимальное количество лопастей: " << (N - 1);
}

#include <iostream>
using namespace std;

int main() {
  setlocale(LC_ALL, "ru");
  long long M;
  cout << "Введите M: ";
  cin >> M;
  if (M < 0) {
    cout << "Значение отрицательное!";
    return 1;
  }
  long long l4 = M % 3;
  long long l3 = (M - 4 * l4) / 3;
  if (l3 >= 0) {
    cout << "С тремя лопастями: " << l3 << endl;
    cout << "С четырьмя лопастями: " << l4 << endl;
  } else {
    cout << 0 << endl;
    cout << 0 << endl;
  }
  return 0;
}

#include <iostream>
using namespace std;

// O(n^4)
int main() {
  setlocale(LC_ALL, "ru");
  long long N, M;

  cin >> N;
  cout << endl;
  cin >> M;
  int k = 0;

  for (int i = 0; i < N; i++) {
    for (int j = i; j < N; j++) {
      for (int a = 0; a < M; a++) {
        for (int b = a; b < M; b++) {
          k++;
        }
      }
    }
  }
  cout << k;
}

#include <iostream>
using namespace std;

int main() {
  setlocale(LC_ALL, "ru");
  long long N, M;
  cout << "Введите N: ";
  cin >> N;
  cout << "Введите M: ";
  cin >> M;
  if (N < 0 or M < 0) {
    cout << "Отрицательное значение!";
    return 1;
  }
  long long kx = 0;
  long long ky = 0;
  for (int x1 = 0; x1 < N; x1++) {
    kx += N - x1;
  }
  for (int y1 = 0; y1 < M; y1++) {
    ky += M - y1;
  }
  cout << "Ответ: " << kx * ky << endl;
  return 0;
}

#include <iostream>
using namespace std;

int seats(int a) {
  if (a <= 36) {
    return (a - 1) / 4;
  }
  return 8 - (a - 37) / 2;
}
int main() {
  setlocale(LC_ALL, "ru");
  int N, seat;
  int coupe[9] = {0};
  cout << "Введите N: ";
  cin >> N;
  if (N < 0) {
    cout << "Значение отрицательное!";
    return 1;
  }
  for (int i = 0; i < N; i++) {
    cout << ">>: ";
    cin >> seat;
    if (seat < 0 or seat > 54) {
      cout << "Таких мест не существует!" << endl;
      i--;
      continue;
    }
    int a = seats(seat);
    coupe[a]++;
  }
  int count = 0;
  int result = 0;
  for (int i = 0; i < 9; i++) {
    if (coupe[i] == 6) {
      count++;
      result = max(result, count);
    } else {
      count = 0;
    }
  }
  cout << endl;
  cout << "Ответ: " << result << endl;
  return 0;
}

#include <iostream>
using namespace std;

int main() {
  setlocale(LC_ALL, "ru");
  long long N, K;
  cout << "Введите N: ";
  cin >> N;
  cout << "Введите K: ";
  cin >> K;
  if (K > N) {
    cout << "Не удовлетворяет условию!";
    return 1;
  }
  if (K <= 0 or N <= 0) {
    cout << "Значение не удовлетворяют условию!";
    return 1;
  }
  while (K != 1) {
    N = (N - K % 2) / 2;
    K = K / 2;
  }
  cout << "Ответ 1: " << (N - 1) / 2 << endl;
  cout << "Ответ 1: " << N / 2 << endl;
  return 0;
}
