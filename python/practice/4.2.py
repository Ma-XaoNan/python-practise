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