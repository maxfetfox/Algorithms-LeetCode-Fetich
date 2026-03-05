from random import randint
import datetime


def randomized_partition(arr: list, low: int, high: int) -> int:
    rand = randint(low, high)
    arr[high], arr[rand] = arr[rand], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_select(arr: list, low: int, high: int, k: int) -> int:
    if low < high:
        q = randomized_partition(arr, low, high)
        if q > k:
            return quick_select(arr, low, q - 1, k)
        elif q < k:
            return quick_select(arr, q + 1, high, k)
        else:
            return arr[q]
    return arr[low]


time_now = datetime.datetime.now()
lst = [6, 3, 4, 6, 8, 1, 34, 67, 45]
print(quick_select(lst, 0, 8, 3))
print(datetime.datetime.now() - time_now)


