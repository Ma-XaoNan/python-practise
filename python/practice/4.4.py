#字符串
my_str = "congratulations and well done!"

value = my_str[2]
value2 = my_str[-16]
print(value)
print(value2)

#my_str[2] = "H"

#index()方法
num = my_str.index("and")
print(f"在字符串{my_str}中查找and，其初始下标是{num}")
#replace()方法
new_str = my_str.replace("and", "or")
print(f"将字符串{my_str}中的and替换为or，得到的新字符串是{new_str}")
#split()方法
my_str = "apple,banana,orange"
new_my_str = my_str.split(",")
print(f"将字符串{my_str}以,分割，得到的列表是{new_my_str}")
#strip()方法
my_str = "  apple, banana, orange  "#不传入参数时默认去除两端空格
new_my_str = my_str.strip()
print(f"将字符串{my_str}两端的空格去除，得到的新字符串是{new_my_str}")

my_str = "122apple, banana, orange21"
new_my_str = my_str.strip("12")
print(f"将字符串{my_str}两端的12去除，得到的新字符串是{new_my_str}")

#统计字符串中某个字符串的出现次数
my_str = "apple,banana,orange,banana,pear"
count = my_str.count("banana")
print(f"字符串{my_str}中出现了{count}次banana")

#统计字符串的长度
my_str = "hello world"
length = len(my_str)
print(f"字符串{my_str}的长度是{length}")

#练习
my_str = "apple,banana,orange,banana,pear"
#统计字符串中an的出现次数
count = my_str.count("an")
print(f"字符串{my_str}中出现了{count}次an")
#将字符串内的空格替换为｜
new_str = my_str.replace(",", "|")
print(f"将字符串{my_str}内的,替换为｜，得到的新字符串是{new_str}")
#将字符串以｜分割，得到列表
new_list = new_str.split("|")
print(f"将字符串{my_str}以｜分割，得到的列表是{new_list}")