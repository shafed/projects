#include <cmath>
#include <iostream>
#include <string>
using namespace std;

int to10(string s, int base) {
  int n10 = 0;
  int i = s.size() - 1;
  int dig;
  for (char c : s) {
    if (c >= '0' && c <= '9')
      dig = c - '0';
    else {
      dig = c - 'A' + 10;
    }
    if (dig >= base) {
      cout << "Недопустимая цифра для системы счисления";
      exit(-1);
    } else {
      n10 += dig * pow(base, i);
    }
    i--;
  }
  return n10;
}

string tonew(int n, int base) {
  string s = "";
  int left;
  while (n > 0) {
    left = n % base;
    if (left < 10) {
      s = char('0' + left) + s;
    } else {
      s = char('A' + (left - 10)) + s;
    }
    n /= base;
  }

  return (s != "") ? s : "0";
}

int main() {
  cout << "КВБО-11-25 Шапаренко Фёдор Александрович" << endl;
  cout << "Практическое задание №4" << endl;
  cout
      << R"(Программа должна считывать с клавиатуры число, записанное в одной системе счисления, и выводить на экран это число в записи по другому основанию, например: исходное
число – 112D, старое основание – 16, новое основание – 8, результат – 10455)"
      << endl;
  string s;
  int old, base;
  cout << "Введите число, старое и новое основание: ";
  cin >> s >> old >> base;
  for (int i = 0; i < s.size(); i++) {
    s[i] = toupper(s[i]);
  }

  cout << "Число в " << base << " системе счисления: ";
  if (base == 10) {
    cout << to10(s, old);
  } else {
    cout << tonew(to10(s, old), base);
  }
}
