#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void nuli(string n) {
  if (n.length() == 1)
    cout << n;
  else {
    while (n[0] == '0') {
      n = n.substr(1);
    }
    if (n.length() == 0)
      cout << '0';
    else
      cout << n;
  }
  // 0102 -> 102
  // 012 -> 12
  // 0 -> 0
  // 000 -> 0
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №3" << endl;
  cout
      << R"(Условие: Вывести на экран только числа из созданного Вами на диске текстового файла, содержащего буквы и числа)"
      << endl;

  ofstream fout("digit.txt");
  if (fout.is_open()) {
    fout << "adf000asjj123jkljj0asjfjfd0102ksjfklj012kjaj11jjk0000jjk0500"
         << endl;
    fout.close();
  } else {
    cout << "Error";
    return 1;
  }

  ifstream fin("digit.txt");

  if (!fin.is_open()) {
    cout << "Error" << endl;
    return 1;
  }

  string line, n = "";
  while (getline(fin, line)) {
    for (int i = 0; i < line.length(); i++) {
      if (isdigit(line[i]))
        n += line[i];
      else {
        if (n != "") {
          if (n[0] != '0' || n.length() == 1)
            cout << n;
          else
            nuli(n);
          n = "";
        }
      }
    }
  }

  if (n != "") {
    if (n[0] != '0' || n.length() == 1)
      cout << n;
    else
      nuli(n);
  }

  fin.close();
  return 0;
}
