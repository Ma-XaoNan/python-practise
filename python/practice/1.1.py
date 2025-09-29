class_sum = 57
avg_salary = 60000
message = "学IT来：%s，工资%s"% (class_sum ,  avg_salary)
print(message)


num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345不限制，小数精度2，结果是：%.2f" % num2)

name = "你好啊"
set_up = 2006
srock_price = 19.99
#f:format
print(f"{name}，你在{set_up}年购买的《石头记》一共花了{srock_price}元。")

print("1*1 的结果是：%d"%(1*1))
print(f"1*2 的结果是：{1*2}")
print("字符串在python中的类型名是：%s"%(type("String")))

name = "小明"
stock_price = 2006
stock_code = "000001"
xi_shu = 1.3
day = 7
stock_price_after = 3000
print(f"{name}在{stock_price}年买入{stock_code}股票，系数为{xi_shu},买入{day}天后，股票价格为{stock_price_after}元。")

print ("请告诉我你是谁")
name = input()
print(f"我知道了你是{name}")