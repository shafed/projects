#include <fstream>
#include <iostream>
#include <string>
using namespace std;

void ascii() {
  ifstream fin("text.txt");
  ifstream fin_copy("text.txt");
  if (!fin.is_open() || !fin_copy.is_open()) {
    cout << "Error 1";
    exit(1);
  }
  string line;
  while (getline(fin, line)) {
    cout << line << endl;
  }
  while (getline(fin_copy, line)) {
    for (char c : line) {
      cout << int(c) << endl;
    }
  }
  fin.close();
}

void entrance() {
  int cnt[256] = {0};
  ifstream fin("text.txt");
  if (!fin.is_open()) {
    cout << "Error 1";
    exit(1);
  }
  string line;
  while (getline(fin, line)) {
  }
}

int main() {
  ascii();
  entrance();
}
