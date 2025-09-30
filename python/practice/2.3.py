#continue
# for i in range(1, 10):
#     print("语句1")
#     for j in range (1,10):
#         print("语句3")
#         continue
#         print("语句2")

#break
# for i in range(1, 10):
#     print("语句1")
#     for j in range (1,10):
#         print("语句3")
#         break
#         print("语句2")

#某公司，账户余额有1W元，给20名员工发工资。
#员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
#领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
#如果工资发完了，结束发工资。
money = 10000
for i in range(1, 21):
    import random
    score = random.randint(1, 10)
    if score < 5:
        print(f"员工{i}的绩效分{score}不足，不发工资，下一位")
        continue
    if money >= 1000:
        money -= 1000
        print(f"员工{i}领取了1000元，公司账户余额：{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不足以发工资")
        break

