#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №3" << endl;
  cout
      << R"(Условие: Создать на диске текстовый файл и скопировать его на экран.)"
      << endl;

  ofstream fout("file.txt");
  if (fout.is_open()) {
    fout << "Hello, world!" << endl;
    fout << "This is myi first file." << endl;
    fout << "C++ will nowread and print it." << endl;
    fout.close();
  } else {
    cout << "Error";
    return 1;
  }

  ifstream fin("file.txt");
  string line;
  if (fin.is_open()) {
    while (getline(fin, line)) {
      cout << line << endl;
    }
    fin.close();
  } else {
    cout << "Error";
    return 1;
  }
  return 0;
}
