from random import randint
import datetime


# алгоритм Lomuto
def randomized_partition(arr: list, low: int, high: int) -> int:
    rand = randint(low, high) # выбор индекса для pivot
    arr[high], arr[rand] = arr[rand], arr[high] # обмен для сравнения pivot с другими элементами
    pivot = arr[high]
    i = low - 1 # индекс последнего элемента в зоне элементов <= pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # перестановка текущего элемента <= pivot в левую часть
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # возвращение pivot на правую границу элементов <= pivot
    return i + 1

def quick_sort(arr: list, low: int, high: int) -> list:
    if low < high:
        q = randomized_partition(arr, low, high)
        # рекурсии, чтобы продолжать разделять массив, в связи с чем происходит сортировка
        quick_sort(arr, low, q - 1)
        quick_sort(arr, q + 1, high)
    return arr

time_now = datetime.datetime.now()
lst = [6, 3, 4, 6, 8, 1, 34, 67, 45]
print(quick_sort(lst, 0, len(lst) - 1))
print(datetime.datetime.now() - time_now)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]