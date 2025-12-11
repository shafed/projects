#include <cmath>
#include <iostream>
using namespace std;

// Insertion Sort
void insertionSort(int arr[], int left, int right) {
  for (int i = left + 1; i <= right; i++) {
    int key = arr[i];
    int j = i - 1;

    // Сдвигаем элементы больше key вправо
    while (j >= left && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}

// Обмен двух элементов
void swap(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

// Максимум в корне
void heapify(int arr[], int n, int i) {
  int largest = i;       // Индекс наибольшего элемента
  int left = 2 * i + 1;  // Левый потомок
  int right = 2 * i + 2; // Правый потомок

  // Если левый потомок больше корня
  if (left < n && arr[left] > arr[largest])
    largest = left;

  // Если правый потомок больше наибольшего элемента
  if (right < n && arr[right] > arr[largest])
    largest = right;

  // Если наибольший элемент не корень
  if (largest != i) {
    swap(arr[i], arr[largest]);
    // Рекурсия для поддерева
    heapify(arr, n, largest);
  }
}

// HeapSort
void heapSort(int arr[], int left, int right) {
  int n = right - left + 1;

  // Строим кучу (перегруппировываем массив)
  for (int i = n / 2 - 1; i >= 0; i--)
    heapify(arr + left, n, i);

  // Извлекаем элементы из кучи один за другим
  for (int i = n - 1; i > 0; i--) {
    swap(arr[left], arr[left + i]);
    heapify(arr + left, i, 0);
  }
}

// QuickSort
int partition(int arr[], int left, int right) {
  // Выбираем опорный элемент (pivot) - последний элемент
  int pivot = arr[right];
  int i = left - 1; // Индекс меньшего элемента

  for (int j = left; j < right; j++) {
    // Если текущий элемент меньше или равен pivot
    if (arr[j] <= pivot) {
      i++;
      swap(arr[i], arr[j]);
    }
  }
  swap(arr[i + 1], arr[right]);
  return i + 1;
}

// Основная функция интроспективной сортировки
void introsortHelper(int arr[], int left, int right, int depthLimit) {
  int size = right - left + 1;

  // Если размер <= 16, используем сортировку вставками
  if (size <= 16) {
    insertionSort(arr, left, right);
    return;
  }

  // Если превышена максимальная глубина рекурсии, используем heapsort
  if (depthLimit == 0) {
    heapSort(arr, left, right);
    return;
  }

  // Иначе используем quicksort
  int pivot = partition(arr, left, right);

  // Рекурсивно сортируем части
  introsortHelper(arr, left, pivot - 1, depthLimit - 1);
  introsortHelper(arr, pivot + 1, right, depthLimit - 1);
}

// Главная функция интроспективной сортировки
void introsort(int arr[], int n) {
  // Максимальная глубина рекурсии = 2 * log2(n)
  int depthLimit = 2 * log2(n);
  introsortHelper(arr, 0, n - 1, depthLimit);
}

int main() {
  int arr[] = {64, 34, 25, 12, 22, 11, 90, 88, 45, 50, 32, 76, 15, 8, 99, 3};
  int n = sizeof(arr) / sizeof(arr[0]);

  cout << "Исходный массив: ";
  for (int i = 0; i < n; i++)
    cout << arr[i] << " ";
  cout << endl;

  introsort(arr, n);

  cout << "Отсортированный массив: ";
  for (int i = 0; i < n; i++)
    cout << arr[i] << " ";
  cout << endl;

  return 0;
}
