def knapsack_greedy(n, M, weights, profits):
    # 计算单位重量价值
    value_per_weight = [(profits[i] / weights[i], i) for i in range(n)]
    value_per_weight.sort(reverse=True)  # 按照单位重量价值降序排序

    # 初始化背包容量和最大收益
    current_capacity = M
    max_profit = 0  
    chosen_items = []

    # 贪心选择物品放入背包
    for value_weight, item_index in value_per_weight:
        if current_capacity >= weights[item_index]:
            chosen_items.append(item_index)
            max_profit += profits[item_index]
            current_capacity -= weights[item_index]

    return chosen_items, max_profit

# 示例调用
n = 7  # 物品数量
M = 15  # 背包容量
weights = [2, 3, 5, 7, 1, 4, 1]  # 物品重量
profits = [10, 5, 15, 7, 6, 18, 13]  # 物品收益

chosen_items, max_profit = knapsack_greedy(n, M, weights, profits)

# 输出最优解和最大收益
print("最优解（选择的物品索引）:", chosen_items)
print("最大收益:", max_profit)


# knapsack_greedy函数使用贪心算法解决背包问题。
# 首先计算每个物品的单位重量价值，并按照单位重量价值的降序对物品进行排序。然后依次选择单位重量价值最高的物品，
# 如果该物品的重量小于等于当前背包容量，则将其放入背包，并更新当前背包容量和最大收益。
# 最后返回选择的物品索引列表和最大收益。
# 在示例调用中，给定了物品数量n、背包容量M、物品的重量列表weights和物品的收益列表profits。调用knapsack_greedy函数求解最优解和最大收益，并将结果打印输出。