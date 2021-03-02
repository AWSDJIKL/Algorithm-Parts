# 随机梯度下降法
# 模拟使用随机梯度下降法来训练函数参数
# 函数为y=w*x

import numpy as np
import matplotlib.pyplot as plt
import random


# 函数
def f(w, x):
    return w * x


# 误差函数，c=(y-y_hat)²/2
# 随机梯度下降只取单个样本计算
def cost(w, x, y):
    c = (y - f(w, x)) ** 2 / 2
    return c


# 求梯度，即误差函数对w求导
# 随机梯度下降只取单个样本计算
def gradient(w, x, y):
    g = (w * x - y) * x
    return g


# 样本数据
xs = [1, 2, 3, 4, 5, 6]
ys = [2, 4, 6, 8, 10]
w = 1  # w初始值
a = 0.01  # 学习效率,每次
w_list = []  # 记录w变化
cost_list = []  # 记录损失变化

sample = list(zip(xs, ys))
# 迭代修改w
for epoch in range(100):
    random.shuffle(sample)
    for x, y in sample:
        w_list.append(w)
        cost_list.append(cost(w, x, y))
        w -= a * gradient(w, x, y)
print(w_list)
print(cost_list)
plt.plot(np.asarray(w_list), np.asarray(cost_list))
plt.show()
