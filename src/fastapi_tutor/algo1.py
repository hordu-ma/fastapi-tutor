# 各种时间复杂度的示例


def time_complexity_examples(n):
    # O(1) - 常数时间复杂度
    def get_first_element(arr: list) -> int:
        return arr[0]  # 直接访问第一个元素

    first_element = get_first_element([1, 2, 3, 4, 5])
    print(f"O(1) - First element: {first_element}")

    # O(n) - 线性时间复杂度
    def linear_search(arr: list, target: int) -> int:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1

    index = linear_search([1, 2, 3, 4, 5], 3)
    print(f"O(n) - Index of target: {index}")

    # O(n^2) - 二次时间复杂度(冒泡排序)
    def bubble_sort(arr: list) -> list:
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    sorted_array = bubble_sort([5, 3, 1, 4, 2])
    print(f"O(n^2) - Sorted array: {sorted_array}")

    # O(log n) - 对数时间复杂度(二分查找)
    def binary_search(arr: list, target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    index = binary_search([1, 2, 3, 4, 5], 4)
    print(f"O(log n) - Index of target: {index}")

    # O(n log n) - 线性对数时间复杂度(归并排序)
    def merge_sort(arr: list) -> list:
        if len(arr) > 1:
            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]

            merge_sort(left_arr)
            merge_sort(right_arr)

            i = j = k = 0

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1
        return arr

    sorted_array = merge_sort([5, 3, 1, 4, 2])
    print(f"O(n log n) - Sorted array: {sorted_array}")


if __name__ == "__main__":
    n = 10
    time_complexity_examples(n)

# 运行结果示例:
# O(1) - First element: 1
# O(n) - Index of target: 2
# O(n^2) - Sorted array: [1, 2, 3, 4, 5]
# O(log n) - Index of target: 3
# O(n log n) - Sorted array: [1, 2, 3, 4, 5]
