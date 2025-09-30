str1 = "Hello"
str2 = "World"
str3 = "dawdeda"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}长度为{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}长度为{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}长度为{count}")


# 定义一个函数来计算字符串长度
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}长度为{count}")

my_len(str1)
my_len(str2)
my_len(str3)
