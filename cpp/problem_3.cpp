#include <iostream>
using namespace std;

int main() {
  long long n, m, cnt = 0;
  cout << "Введите N и M: ";
  cin >> n >> m;
  if (n <= 0 || m <= 0) {
    cout << "Количество прямоугольников: 0";
    return 1;
  }
  for (long long h = 1; h <= n; h++) {
    long long vert = n - h + 1;
    for (long long w = 1; w <= m; w++) {
      long long hor = m - w + 1;
      cnt += vert * hor;
    }
  }
  cout << "Количество прямоугольников: " << cnt;
  return 0;
}
