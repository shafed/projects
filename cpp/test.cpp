#include <cmath>
#include <iostream>
#include <string>
#include <vector>

int main() {
  // Диапазон и шаг
  double x_start = -10;
  double x_end = 10;
  double x_step = 0.5;

  // Размеры терминала
  int width = 40;
  int height = 20;

  // Создание матрицы
  std::vector<std::string> screen(height, std::string(width, ' '));

  // Нарисовать оси
  for (int i = 0; i < height; ++i) {
    screen[i][width / 2] = '|';
  }
  for (int i = 0; i < width; ++i) {
    screen[height / 2][i] = '-';
  }
  screen[height / 2][width / 2] = '+';

  // Нарисовать график функции
  for (double x = x_start; x <= x_end; x += x_step) {
    double y = std::sin(x); // Пример функции

    // Преобразование координат в индексы
    int col = static_cast<int>((x - x_start) / (x_end - x_start) * width);
    int row =
        height / 2 - static_cast<int>(y / 10 * height /
                                      2); // Предполагая, что y от -10 до 10

    if (col >= 0 && col < width && row >= 0 && row < height) {
      screen[row][col] = '*';
    }
  }

  // Вывод графика
  for (const auto &row : screen) {
    std::cout << row << std::endl;
  }

  return 0;
}
