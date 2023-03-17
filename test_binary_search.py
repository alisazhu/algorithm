# 二分查找法的逻辑

import pytest

"""
时间复杂度：对于存在列表中的元素，查找最多需要log2N而对于不再列表中的元素则需要log2N+1,原因是因为在列表中时，则需要将最终的元素也进行对比
"""


def binary_search(lo, item):
    low = 0
    high = len(lo) - 1
    i = 0
    while low <= high:
        mid = (low + high) // 2  # 这里要使用底板除才可以用作list的下标

        if item == lo[mid]:
            return mid, i
        elif item < lo[mid]:
            high = mid - 1
        else:
            low = mid + 1
        i += 1

    return None





def test_binary_search():
    lo = [1, 2, 3, 4, 5, 6, 7, 8]
    item = 8
    k, i = binary_search(lo, item)

    print(k, i)

# if __name__ == '__main__':
#     lo = [1, 2, 3, 4, 5, 6, 7, 8]
#
#     k, i = binary_search(lo, 8)
#
#     print(k, i)
