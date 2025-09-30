# • 定义一个全局变量：money，用来记录银行卡余额（默认5000000）
# • 定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
# • 定义如下的函数：
# • 查询余额函数
# • 存款函数
# • 取款函数
# • 主菜单函数
# • 要求：
# • 程序启动后要求输入客户姓名
# • 查询余额、存款、取款后都会返回主菜单
# • 存款、取款后，都应显示一下当前余额
# • 客户选择退出或输入错误，程序会退出，否则一直运行
money = 5000
name = input("请输入您的姓名：")

def query_balance():
    print("您的余额为：", money)
    return main_menu()

def deposit():
    global money
    money += int(input("请输入存款金额："))
    print("您的余额为：", money)
    return main_menu()

def withdraw():
    global money
    money -= int(input("请输入取款金额："))
    if money < 0:
        print("您的余额不足，取款失败！")
        return main_menu()
    print("您的余额为：", money)
    return main_menu()

def main_menu():
    print("1. 查询余额")
    print("2. 存款")
    print("3. 取款")
    print("4. 退出")
    choice = input("请选择：")
    if choice == "1":
        return query_balance()
    elif choice == "2":
        return deposit()
    elif choice == "3":
        return withdraw()
    elif choice == "4":
        print("欢迎下次光临！")
        exit()
    else:
        print("输入错误，请重新输入！")
        return main_menu()

main_menu()