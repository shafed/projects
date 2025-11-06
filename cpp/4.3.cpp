#include <cmath>
#include <iostream>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout << R"(Условие: Вывести на экран график функции у = sin x)" << endl;

  float pi = M_PI;
  int w = 30, h = 15;
  for (int y = h; y >= -h; y--) {
    for (int x = -w; x < w; x++) {
      float angle = x * pi / w;
      int calc_sin = (int)(sin(angle) * h);

      if (x == 0 and y == 0)
        cout << "+";
      else if (x == 0)
        cout << "|";
      else if (y == 0)
        cout << "-";
      else if (y == calc_sin) {
        cout << "*";
      } else
        cout << " ";
    }
    cout << endl;
  }
}
