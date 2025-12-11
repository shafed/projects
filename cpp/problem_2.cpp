#include <iostream>
using namespace std;

int main() {
  long long M;
  cin >> M;

  if (M < 0) {
    cout << "Отрицательное значение!" << endl;
    return 1;
  }

  long long left = M % 3;
  long long cnt3 = (M - 4 * left) / 3;

  if (cnt3 >= 0) {
    cout << "С тремя лопастями: " << cnt3 << endl;
    cout << "С четырьмя лопастями: " << left << endl;
  } else {
    cout << "С тремя лопастями: 0" << endl;
    cout << "С четырьмя лопастями: 0" << endl;
  }
  return 0;
}
