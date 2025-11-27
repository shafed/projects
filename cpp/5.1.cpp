#include <iostream>
#include <string>
using namespace std;

int transfer(char c) {
  if (c == 'I')
    return 1;
  else if (c == 'V')
    return 5;
  else if (c == 'X')
    return 10;
  else if (c == 'L')
    return 50;
  else if (c == 'C')
    return 100;
  else if (c == 'D')
    return 500;
  else if (c == 'M')
    return 1000;
  return -1;
}

int main() {

  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout << R"(Декодировать римскую запись
числа, состоящего из любого количества знаков. Правила: I→1, V→5, X→10,
L→50, C→100, D→500, M→1000. Значение римской цифры не зависит от
позиции, а знак –- зависит.)"
       << endl;
  string s;
  cout << "Введите римское число: ";
  cin >> s;

  int ttl = 0;

  for (int i = 0; i < s.size(); i++) {
    s[i] = toupper(s[i]);
  }

  for (int i = 0; i < s.size(); i++) {
    int now = transfer(s[i]);

    if (now == -1) {
      cout << "Неверный символ";
      return 1;
    }

    if (i < s.size() - 1 && now < transfer((s[i + 1]))) {
      ttl -= now;
    } else {
      ttl += now;
    }
  }

  cout << "Арабское число: " << ttl << endl;
}
