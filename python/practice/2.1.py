#1~100的和
# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(sum)

#设置一个范围1-100的随机整数，通过while循环，配合input语句，判断输入的数字是否等于随机数
# import random
# num = random.randint(1, 100)
# flag = True
# count = 0
# while flag:
#     guess = int(input("请输入一个1-100之间的整数："))
#     count += 1
#     if guess == num:
#         print("恭喜你，猜对了！")
#         #设置为fales就是终止循环
#         flag = False
#     elif guess < num:
#         print("猜的数字小了，请再试一次！")
#     else:
#         print("猜的数字大了，请再试一次！")
# print(f"你总共猜了{count} 次")

#内外层嵌套循环
# i = 1
# while i<=100:
#     print(f"今天是第{i}天，准备表白")
#     j = 1
#     while j<=10:
#         print(f"第{j}次表白")
#         j += 1
#     print("我喜欢你")
#     i = i+1
# print(f"坚持到第{i-1}天，表白成功")

#打印九九乘法表
# i = 1
# while i<=9:
#     j = 1
#     while j<=i:
#         print(f"{j}*{i}={i*j}", end="\t")
#         j += 1
#     print()
#     i += 1


#for循环
# count = 0
# name = "QWERTFDSAZSWERGFDSAS"
# for i in name:
#     if i == "S":
#         count += 1
# print(count)

#range语法1 range(num)
# for x in range(10):
#     print(x)

#range语法2 range(start, end)
# for x in range(5, 10):
#     print(x)

#range语法3 range(start, end, step)
for x in range(5, 10, 2):
    print(x)
