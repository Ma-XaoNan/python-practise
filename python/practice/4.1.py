# my_list = ["qwq","wewq","qweqwe"]
# print(my_list)
# print(type(my_list))
#
# my_list = ["qwq",1231,True]
# print(my_list)
# print(type(my_list))

my_list = ["qwq",True,1231,"wewq"]
# print(my_list)
# print(type(my_list))
#
# # print(my_list[0])
# # print(my_list[1])
# # print(my_list[2])
# print(my_list[0][1])
index = my_list.index("qwq")
print(index)

my_list2 = ["wewq","qweqwe","wewq"]
#修改元素
my_list[0] = "qwqqwq"
print(my_list)

#插入元素
my_list.insert(1,"wewq")
print(my_list)

#追加元素
my_list.append("qwq")
print(my_list)

#删除元素
my_list.remove("wewq")
print(my_list)
my_list.pop(1)
print(my_list)
del my_list[0]
print(my_list)
my_list.clear()
print(my_list)

#追加其他数据容器
my_list.extend(my_list2)
print(my_list)

#统计元素个数
my_list = ["qwq",True,1231,"wewq"]
count = my_list.count("wewq")
print(count)

#统计列表总共有多少元素
count = len(my_list)
print(count)