# 读取输入数据
n, k = map(int, input().split())  # 读取总行驶距离n和加油站数量k
a = [0] + [int(x) for x in input().split()]  # 读取k+1个加油站的位置

# 初始化变量
d = n  # 当前剩余里程数
count = 0  # 加油次数
b = [0] * (k + 1)  # 标记列表,记录哪些站需要加油
flag = True  # 标记是否能够顺利到达终点

# 遍历加油站,确定加油策略
for i in range(1, k + 2):
    # 检查当前剩余里程是否足以到达下一个加油站
    if d >= a[i]:
        d -= a[i]  # 更新剩余里程
    else:
        d = n  # 将剩余里程重置为总行驶距离
        if d < a[i]:
            # 如果即使加满油也无法到达当前加油站,则无法到达终点
            flag = False
            break
        count += 1  # 加油次数加1
        b[i - 1] = 1  # 标记当前加油站需要加油
        d -= a[i]  # 更新剩余里程

# 输出结果
if not flag:
    print("No Solution!")  # 无法到达终点
else:
    for i in range(1, k + 2):
        if b[i - 1] == 1:
            print(f"第{i}站需要加油!")  # 输出需要加油的加油站
    print(count)  # 输出最少加油次数