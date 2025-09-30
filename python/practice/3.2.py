def say_hello():
    print("hello")

def add(x,y):
    result = x+y
    print(f"{x} + {y} = {result}")

#掌握返回值
def add_and_return(x,y):
    """
    返回两个数的和
    :param x:
    :param y:
    :return:
    """
    result = x+y
    return result
r = add_and_return(1,2)
print(r)

def say_hi():
    print("hi")
result = say_hi()
print(f"无返回值函数的返回值是{result}")
print(f"我返回值函数，返回的类型是{type(result)}")

def say_hi2():
    print("hi2")
    return None
result = say_hi2()
print(f"无返回值函数的返回值是{result}")
print(f"无返回值函数，返回的类型是{type(result)}")

def check_age(age):
    if age >= 18:
        return True
    else:
        return None
result = check_age(16)
if not result:
    print("你还未成年")

