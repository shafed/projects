#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №3" << endl;
  cout << R"(Условие: Создать файл, записать в него 10 чисел, закрыть, потом
вновь открыть файл и найти сумму чисел.)"
       << endl;

  ofstream fout("numbers.txt");
  if (!fout.is_open()) {
    cout << "Error";
    return 1;
  }
  for (int i = 0; i < 10; i++) {
    double temp;
    cout << "Введите " << i + 1 << "-ое число:";
    cin >> temp;
    fout << temp << endl;
  }
  fout.close();

  ifstream fin("numbers.txt");
  if (!fin.is_open()) {
    cout << "Error";
    return 1;
  }
  string s;
  double sum = 0;
  while (getline(fin, s)) {
    sum += stod(s);
  }

  cout << s << endl;
  cout << sum << endl;
  fin.close();

  return 0;
}
