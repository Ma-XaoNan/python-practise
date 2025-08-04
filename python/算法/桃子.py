def peach_recursive(n):
    if n == 1:
        return 1
    else:
        return 2 * (peach_recursive(n - 1) + 1)

# 示例调用
n = 5
total_peaches = peach_recursive(n)
print("总桃子数:", total_peaches)


# peach_recursive函数使用递归方式实现了求解桃子问题的逻辑。当n为1时，表示到达第1天，只剩下一个桃子，直接返回1作为总桃子数。
#否则，根据递归关系，递归调用peach_recursive函数，将n减1，并将结果乘以2，然后再加上1，得到第n天的总桃子数。
# 在示例调用中，我们传入了n为5，即求解第5天剩下的桃子数量，并将结果打印输出。