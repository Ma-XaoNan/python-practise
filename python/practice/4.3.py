#元组
#元组是不可变的，因此不能修改元组中的元素。
#元组的元素用逗号隔开，并在括号中表示。
#元组的索引从0开始，可以访问元组中的元素。
#元组的长度是元组中元素的个数。
#元组的操作：

#1. 创建元组：
t1 = (1, 2, 3, 4, 5)
t2 = ('a', 'b', 'c', 'd')
t3 = tuple()
print(f"t1类型是{type(t1)}, 内容是{t1}")
print(f"t2类型是{type(t2)}, 内容是{t2}")
print(f"t3类型是{type(t3)}, 内容是{t3}")

t4 = (1,)  # 只有一个元素的元组
print(f"t4类型是{type(t4)}, 内容是{t4}")
t5 = ((1, 2), (3, 4), (5, 6))  # 嵌套元组
print(f"t5类型是{type(t5)}, 内容是{t5}")

num = t5[0][1]
print(f"t5的第1个元素的第2个元素是{num}")

#2. 访问元组元素：
t6 = (1, 2, 3, 4, 5)
index = t6.index(3)
print(f"t6的第中查找3的下标是{index}")

t7 = (1, 2, 3,3, 4, 5)
t7.count(3)
print(f"t7中3出现的次数是{t7.count(3)}")

t8 = (1, 2, 3, 4, 5)
num =len(t8)
print(f"t8的长度是{num}")

index = 0
while index < len(t8):
    print(t8[index])
    index += 1

for i in t8:
    print(i)