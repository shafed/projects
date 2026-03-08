#include <stdio.h>
#include <stdlib.h>

void printArray(int arr[], int n) { // Функция для вывода массивов
  // Выводим 10 элементов из начала
  printf("\nВ начале: ");
  for (int i = 0; i < 10; i++)
    printf("%d ", arr[i]);

  // Разделитель вывода
  printf("\n");
  for (int i = 0; i < 80; i++)
    printf("—");
  printf("\n");

  // Выводим 10 элементов из середины
  printf("\nВ середине: ");
  for (int i = n / 2; i < n / 2 + 10; i++)
    printf("%d ", arr[i]);

  printf("\n");
  for (int i = 0; i < 80; i++)
    printf("—");
  printf("\n");

  // Выводим 10 элементов из конца
  printf("\nВ конце: ");
  for (int i = n - 10; i < n; i++)
    printf("%d ", arr[i]);

  printf("\n");
  for (int i = 0; i < 80; i++)
    printf("=");
  printf("\n");
}

void bubbleSort(int arr[], int n) { // Функция для сортировки
  for (int i = 0; i < n - 1; i++) {
    for (int j = 0; j < n - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
}

int main() {
  int sizes[] = {1000, 5000, 10000}; // Массив размеров

  for (int i = 0; i < 3; i++) { // Для каждого размера
    int n = sizes[i];
    int arr[n];

    for (int j = 0; j < n; j++) // Заполняем массив
      arr[j] = rand();

    printf("\nМассив размера %i до сортировки:\n", n);
    printArray(arr, n); // Выводим до сортировки

    bubbleSort(arr, n); // Сортируем

    printf("\nМассив размера %i после сортировки:\n", n);
    printArray(arr, n); // Выводим после сортировки
  }

  return 0;
}
