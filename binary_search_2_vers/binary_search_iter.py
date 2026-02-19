def search(nums, target):
    # Предположим, nums отсортирован
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1 # переход к левой половине
        elif nums[mid] < target:
            left = mid + 1 # переход к правой половине
    return -1
