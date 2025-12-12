#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Структура для хранения информации о книге
struct Book {
  string author;
  string title;
  int year;
};

// Функция для создания файла и ввода данных о книгах
void createFile(string filename) {
  ofstream file(filename);
  if (!file.is_open()) {
    cout << "Error 1" << endl;
    return;
  }

  int n;
  cout << "Введите количество книг: ";
  cin >> n;
  cin.ignore(); // Очистка буфера

  for (int i = 0; i < n; i++) {
    string author, title;
    int year;

    cout << endl << "--- Книга " << (i + 1) << " ---" << endl;
    cout << "ФИО автора: ";
    getline(cin, author);
    cout << "Название: ";
    getline(cin, title);
    cout << "Год издания: ";
    cin >> year;
    cin.ignore();

    file << author << endl;
    file << title << endl;
    file << year << endl;
  }

  file.close();
}

// Функция для чтения данных из файла
vector<Book> readFile(string filename) {
  vector<Book> books;
  ifstream file(filename);

  if (!file.is_open()) {
    cout << "Error 1" << endl;
    return books;
  }

  Book book;
  while (getline(file, book.author)) {
    getline(file, book.title);
    file >> book.year;
    file.ignore();
    books.push_back(book);
  }

  file.close();
  return books;
}

// Функция а) - поиск названия книги по автору и году
void findBookByAuthorAndYear(const vector<Book> &books) {
  string author;
  int year;

  cout << "\n--- Поиск книги по автору и году ---" << endl;
  cin.ignore();
  cout << "Введите ФИО автора: ";
  getline(cin, author);
  cout << "Введите год издания: ";
  cin >> year;

  bool found = false;
  for (const auto &book : books) {
    if (book.author == author && book.year == year) {
      cout << "\nНайдена книга: " << book.title << endl;
      found = true;
    }
  }

  if (!found) {
    cout << "\nКнига с такими параметрами не найдена." << endl;
  }
}

// Функция б) - поиск книги со словом "Паскаль"
void findPascalBook(const vector<Book> &books) {
  cout << "\n--- Поиск книги со словом 'Паскаль' ---" << endl;

  bool found = false;
  for (const auto &book : books) {
    // Поиск подстроки (регистр не учитывается через преобразование)
    string titleLower = book.title;
    string searchWord = "паскаль";

    // Приведение к нижнему регистру для сравнения
    for (auto &c : titleLower) {
      c = tolower(c);
    }

    if (titleLower.find(searchWord) != string::npos ||
        titleLower.find("Паскаль") != string::npos ||
        book.title.find("Паскаль") != string::npos ||
        book.title.find("паскаль") != string::npos) {
      cout << "\nНайдена книга!" << endl;
      cout << "Название: " << book.title << endl;
      cout << "Автор: " << book.author << endl;
      cout << "Год издания: " << book.year << endl;
      found = true;
    }
  }

  if (!found) {
    cout << "\nКниги со словом 'Паскаль' не найдены." << endl;
  }
}

// Функция для вывода всех книг
void displayAllBooks(const vector<Book> &books) {
  cout << "\n--- Все книги в библиотеке ---" << endl;
  for (size_t i = 0; i < books.size(); i++) {
    cout << "\nКнига " << (i + 1) << ":" << endl;
    cout << "Автор: " << books[i].author << endl;
    cout << "Название: " << books[i].title << endl;
    cout << "Год: " << books[i].year << endl;
  }
}

int main() {
  string filename = "library.txt";
  int choice;

  do {
    cout << "\n========== МЕНЮ ==========" << endl;
    cout << "1. Создать файл и ввести данные о книгах" << endl;
    cout << "2. Показать все книги" << endl;
    cout << "3. Найти название книги по автору и году" << endl;
    cout << "4. Найти книгу со словом 'Паскаль'" << endl;
    cout << "0. Выход" << endl;
    cout << "Выберите действие: ";
    cin >> choice;

    switch (choice) {
    case 1:
      createFile(filename);
      break;
    case 2: {
      vector<Book> books = readFile(filename);
      if (!books.empty()) {
        displayAllBooks(books);
      }
      break;
    }
    case 3: {
      vector<Book> books = readFile(filename);
      if (!books.empty()) {
        findBookByAuthorAndYear(books);
      }
      break;
    }
    case 4: {
      vector<Book> books = readFile(filename);
      if (!books.empty()) {
        findPascalBook(books);
      }
      break;
    }
    case 0:
      cout << "Выход из программы." << endl;
      break;
    default:
      cout << "Неверный выбор!" << endl;
    }
  } while (choice != 0);

  return 0;
}
