def func_b():
    print(2)
def func_a():
    print(1)
    func_b()
    print(3)

# 全局变量
# num = 10
#
# # 局部变量num
# def test_a ():
#
#     print(num)
# def test_b():
#     print(f"{num}")
# test_a()
# test_b()
# print(num)

num = 10

# 在函数内修改全局变量
def test_a ():
    print(num)
def test_b():
    global num
    num = 500# 全局变量
    print(f"{num}")
test_a()
test_b()
print(num)