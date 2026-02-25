def bubble_sort(nums):
    n = len(nums)
    i = 0
    while i < n:
        were_swapped = False
        for j in range(n - 1, i, -1):
            if nums[j] < nums[j - 1]:
                # элементы меняются местами, если текущий элемент меньше предыдущего
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
                were_swapped = True
        if not were_swapped: # данный флаг обеспечивает ранний выход из цикла, что является хорошей оптимизацией
            break
        i += 1
    return nums
