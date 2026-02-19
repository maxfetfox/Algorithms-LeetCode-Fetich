def search(nums, target, left, right):
    # Предположим, nums отсортирован
    if left > right: # базовый случай, если внутри диапазона пусто (элемент не найден), возвращаем -1
        return -1

    middle = (left + right) // 2

    if nums[middle] == target:
        return middle
    elif nums[middle] > target:
        return search(nums, target, left, middle - 1) # переход к левой половине
    return search(nums, target, middle + 1, right) # переход к правой половине
