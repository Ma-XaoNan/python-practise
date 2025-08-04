def generate_schedule(n):
    if n == 1:
        return [[0, 1]]

    # 递归生成上一轮的比赛日程表
    previous_round = generate_schedule(n - 1)

    # 复制上一轮的比赛日程表，扩展为当前轮的比赛日程表
    current_round = previous_round.copy()

    # 在当前轮的比赛日程表中添加新的比赛对阵
    num_players = 2**n
    for i in range(len(previous_round)):
        match = previous_round[i]
        current_round.append([match[0], match[1] + num_players // 2])
        current_round.append([match[1], match[0] + num_players // 2])

    return current_round

# 示例调用
n = 2  # 2^2 = 4个选手
schedule = generate_schedule(n)
print("比赛日程表:")
for match in schedule:
    print(match)

# 如果当前轮次为第一轮，直接返回包含一场比赛的列表[[0, 1]]。
# 对于其他轮次，先递归生成上一轮的比赛日程表。
# 复制上一轮的比赛日程表，并创建一个新的列表作为当前轮的比赛日程表。
# 在当前轮的比赛日程表中，对于上一轮的每一场比赛，创建两场新的比赛，其中一场的选手编号保持不变，另一场的选手编号加上选手总数的一半。
# 将新生成的比赛添加到当前轮的比赛日程表中。
# 返回当前轮的比赛日程表作为结果。
# 该算法的关键在于利用递归思想，通过复制和扩展上一轮的比赛日程表来生成当前轮的比赛日程表。通过不断递归调用自身，每一轮的比赛日程表会不断扩大，直到生成完整的比赛日程表。
    
# 定义了一个名为generate_schedule的函数，接受一个参数n，表示比赛的轮数。
# 如果n等于1，那么是第一轮比赛，直接返回一个包含一场比赛的列表[[0, 1]]。
# 如果n不等于1，执行递归步骤。
# 通过递归调用generate_schedule(n - 1)生成上一轮的比赛日程表，将其赋值给previous_round变量。
# 复制上一轮的比赛日程表，使用copy()方法创建一个新的列表current_round，作为当前轮的比赛日程表。
# 在当前轮的比赛日程表中添加新的比赛对阵。
# 计算当前轮比赛的选手总数，使用num_players = 2**n表示。
# 使用for循环遍历上一轮的比赛日程表中的每场比赛。
# 对于每场比赛，将其编号为match。
# 创建两场新的比赛，分别为[match[0], match[1] + num_players // 2]和[match[1], match[0] + num_players // 2]。
# 将新的比赛添加到当前轮的比赛日程表current_round中。
# 递归结束后，返回当前轮的比赛日程表current_round。