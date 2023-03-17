def recursion(num):
    """
    实现一个函数，打印出3，2,1等
    :return:
    """
    print(num)

    # 基线条件：如果这个数小于等于1，则结束
    if num <= 1:
        return
    # 递归条件：继续打印
    else:
        recursion(num - 1)


if __name__ == '__main__':
    print(recursion(6))

# """
# 例子原型：在嵌套的盒子中查找钥匙
# """
# from numpy import empty
#
# """
# 方法1：创建一个盒子堆，一直拿出盒子中的小盒子查找，如果是钥匙则结束，如果还是盒子就一直找，直到小盒子没有了
# """
#
#
# def look_key(main_box):
#     pile = main_box.make_a_pile_to_look_through()
#
#     while pile is not empty:
#         box = pile.grab_a_box()
#         for item in box:
#             if item.is_a_box():
#                 pile.append(item)
#             elif item.is_a_key():
#                 print("found the Key")
#
#
# """
# 方法2：递归实现，拿一个盒子，判断是否是钥匙，如果是则结束，如果不是，则继续查找，针对的是一个盒子，方法1是针对盒子堆去实现
# """
#
#
# def look_for_key(box):
#     for item in box:
#         if item.is_a_box():
#             look_for_key()
#         elif item.is_a_key():
#             print("found the key")
