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

bool canminus(int small, int big) {
  if (small == 1)
    return (big == 5 * small or big == 10 * small);
  if (small == 10)
    return (big == 5 * small or big == 10 * small);
  if (small == 100)
    return (big == 5 * small or big == 10 * small);
  return 0;
}

bool canrepeat(char c) {
  return (c == 'I' or c == 'X' or c == 'C' or c == 'M');
}

int main() {

  string s;
  bool minus = false;
  cout << "Введите римское число: ";
  cin >> s;

  int ttl = 0;
  int n;
  int cnt = 1;
  for (int i = 0; i < s.size(); i++) {
    int now = transfer(s[i]);

    // test for symbol
    if (now == -1) {
      cout << "Неверный символ";
      return -1;
    }

    // repeat
    if (i > 0 && now == transfer(s[i - 1])) {
      if (!canrepeat(s[i])) {
        cout << "Нельзя повторять";
        return 1;
      }
      cnt++;
      if (cnt > 3) {
        cout << "Больше 3-ёх повторений" << endl;
        return 1;
      }
    } else
      cnt = 1;

    //+-
    if (i < s.size() - 1 && transfer(s[i + 1]) > now) {
      int next = transfer(s[i + 1]);
      // canminus
      if (!canminus(now, next)) {
        cout << "Нельзя вычитать";
        return 1;
      }

      // double minus
      if (i > 0 && now == transfer(s[i - 1])) {
        cout << "Двойное вычитание";
        return 1;
      }

      ttl -= now;
      minus = true;
    } else {

      // smaller symbol after minus
      if (minus && i > 0 && now >= transfer(s[i - 1])) {
        cout << "Меньший символ после вычитания";
        return 1;
      }
      ttl += now;
      minus = false;
    }
  }
  cout << "Арабское число: " << ttl;

  return 0;
}
