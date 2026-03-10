def merge(arr, left, mid, right):
    # Размеры левой и правой частей
    left_size = mid - left + 1
    right_size = right - mid

    L = [0] * left_size
    R = [0] * right_size

    # Копирование левой части
    for i in range(left_size):
        L[i] = arr[left + i]

    # Копирование правой части
    for j in range(right_size):
        R[j] = arr[mid + j + 1]

    i = 0  # индекс для L
    j = 0  # индекс для R
    k = left  # индекс для arr

    # Слияние L и R в arr
    while i < left_size and j < right_size:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Копирование в arr, если в L остались элементы
    while i < left_size:
        arr[k] = L[i]
        i += 1
        k += 1

    # Копирование в arr, если в R остались элементы
    while j < right_size:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)
