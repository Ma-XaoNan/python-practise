def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 元素存在于数组中，返回索引位置
        elif arr[mid] < target:
            left = mid + 1  # 在右半部分继续查找
        else:
            right = mid - 1  # 在左半部分继续查找

    return "没找到!"  # 元素不存在于数组中

# 示例调用
arr = [-7, -2, 0, 5, 16, 43, 57, 102, 291]
targets = [291, 16, 101]

for target in targets:
    result = binary_search(arr, target)
    if isinstance(result, int):
        print(f"元素 {target} 在数组中的位置: {result}")
    else:
        print(f"元素 {target} 没找到!")


# binary_search函数使用二分查找算法来检索目标元素在已排序数组中的位置。
# 初始时，设置左边界left为数组起始位置，右边界right为数组末尾位置。在每一次循环中，计算中间元素的索引mid，并与目标元素进行比较。
# 如果相等，则返回中间元素的索引；如果目标元素较大，则更新左边界为mid + 1；如果目标元素较小，则更新右边界为mid - 1。
# 如果循环结束时仍未找到目标元素，则返回-1。
# 在示例调用中，给定已排序的数组arr和目标元素列表targets，使用循环依次检索每个目标元素，并根据返回的索引位置输出结果。