#include <iostream>
#include <string>
using namespace std;

int to10(string s, int base) {
  int n = 0;
  for (char c : s) {
    if (c >= '0' && c <= char(10))
      n = else { s.pop_back(); }
  }
}

int main() {
  string s;
  int old, base;
  cout << "Введите число, старое и новое основание: ";
  cin >> s >> old >> base;
}
