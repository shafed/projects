#include <cmath>
#include <iostream>
using namespace std;

void rectangle() {
  cout << "Введите ширину и высоту: ";
  float w, h;
  cin >> w >> h;
  if (w <= 0 || h <= 0)
    cout << "Площади не существует";
  else
    cout << "Площадь прямоугольника равна: " << w * h << endl;
}

void triangle() {
  cout << "Введите основание и высоту: ";
  float a, h;
  cin >> a >> h;
  if (a <= 0 || h <= 0)
    cout << "Площади не существует";
  else
    cout << "Площадь треугольника равна: " << 0.5 * a * h << endl;
}

void circle() {
  cout << "Введите радиус: ";
  float r;
  float pi = M_PI;
  cin >> r;
  if (r <= 0)
    cout << "Площади не существует";
  else
    cout << "Площадь круга равна: " << pi * r * r << endl;
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout
      << R"(Условие: Вычислить площади прямоугольника, треугольника, круга, используя подпрограммы-функции.)"
      << endl;

  rectangle();
  triangle();
  circle();
}
