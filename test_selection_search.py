"""
选择排序：
是一种简单直观的排序算法。工作原理是第一次懂待排序的元素中找到最小的元素，将该元素存储在一个新的序列的起始位置，
以此类推，直到全部待排序的数据元素个数为0
"""


def findSmallest(arr):
    """
    找出数组中最小的元素,并返回下标
    :param arr:
    :return:
    """
    smallest = arr[0]
    smallest_index = 0
    # 1.遍历数组,挨个查找元素，定义一个变量，初始值为数组的第一个元素，
    # 2.之后通过将该元素与数组中的下一个元素进行对比，
    # 3.如果比当前的初始值小，则更新该变量的值，其中需要和数组剩下的元素进行比对
    # 4.剩下的数组的长度的确定，首先需要跟下标为1的元素开始比较，总共n个元素，则需要跟剩下的n-1个元素进行比对
    # 5.len(arr)为数组的长度，而需要比较的数目为1~n-1，即range(1,len(arr))
    for i in range(1, len(arr)):

        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selectionSort(arr):
    """

    :param arr:
    :return:
    """

    new_arr = []

    # 原数组的长度为n,需要将所有的元素都进行排序，则range(len(arr))，等价于range(0,len(arr)),直到原数组的待排序的元素个数为0

    for i in range(len(arr)):
        smallest = findSmallest(arr)

        # 1.找出最小的元素的下标之后，使用pop()函数将元素取出后使用append()放入新的数组中
        # 2.arr.pop()函数的参数为数组的下标
        new_arr.append(arr.pop(smallest))

    return new_arr


if __name__ == '__main__':
    arr = [2, 6, 7, 1, 0, 3]

    sorted_arr = selectionSort(arr)
    print(sorted_arr)
