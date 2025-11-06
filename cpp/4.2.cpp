#include <iostream>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout << R"(Условие: В 1912 году американский флаг «Былая слава»
имел 48 звезд (по одной на каждый штат) и 13 полос (по одной на колонию).
Вывести на экран «Былую славу 1912 года»)"
       << endl;

  for (int i = 0; i < 6; i++) {
    for (int j = 0; j < 8; j++) {
      cout << "* ";
    }
    for (int k = 0; k < 40; k++) {
      cout << "=";
    }
    cout << endl;
  }

  for (int i = 0; i < 7; i++) {
    for (int j = 0; j < 56; j++) {
      cout << "=";
    }
    cout << endl;
  }
}
