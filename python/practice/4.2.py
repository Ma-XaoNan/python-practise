#1. 定义这个列表，并用变量接收它，内容是：［21，25，21，23，22,20]
my_list = [21, 25, 21, 23, 22, 20]

#2. 追加一个数字31，到列表的尾部
my_list.append(31)
print(my_list)
#3.追加一个新列表［29，33，30］，到列表的尾巴部
my_list.extend([29, 33, 30])
print(my_list)
#4.取出第一个元素（应是：21）
print(my_list.pop(0))
print(my_list)
#5. 取出最后一个元素（应是：30）
print(my_list.pop(-1))
print(my_list)
#6. 查找元素31，在列表中的下标位置
print(my_list.index(31))


def list_while_func():
    """
    使用while循环遍历列表的演示函数
    :return:
    """
    my_list = [21, 25, 21, 23, 22, 20]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element)
        index += 1

list_while_func()

def list_for_func():
    """
    使用for循环遍历列表的演示函数
    :return:
    """
    my_list = [21, 25, 21, 23, 22, 20]
    for element in my_list:
        print(element)

list_for_func()

# 定义一个列表，内容是：［12,3,4,5,6,7,8,9,10］
# 遍历列表，取出列表内的偶数，并存入一个新的列表对象中
# 使用while循环和for循环各操作一次
# 迪过whiLe循环，从列表：[1，2，3，4，5，6，7，8，9，10］中取出偶数，组成新列表：［2,4,6,8,10］
# 通过for循环，从列表：［2，2，3，4，5，6，7，8，9，10］中取出偶数，组成新列表：［2，4，6,8,10］
# 提示：
# 通过if判断来确认偶数
# 通过列表的append肪法，来增加元素

my_list = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)

new_list = []
index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        new_list.append(my_list[index])
    index += 1
print(new_list)

