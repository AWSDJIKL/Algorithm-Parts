# 梯度下降法
# 模拟使用梯度下降法来训练函数参数
# 函数为y=w*x

import numpy as np
import matplotlib.pyplot as plt


# 函数
def f(w, x):
    return w * x


# 误差函数，c=(y-y_hat)²/2
def cost(w, xs, ys):
    c = 0
    for x, y in zip(xs, ys):
        c += (y - f(w, x)) ** 2 / 2
    c /= len(ys)
    return c


# 求梯度，即误差函数对w求导
def gradient(w, xs, ys):
    g = 0
    for x, y in zip(xs, ys):
        g += (w * x - y) * x
    g /= len(ys)
    print(g)
    return g


# 样本数据
xs = [1, 2, 3, 4, 5, 6]
ys = [2, 4, 6, 8, 10]
w = 1  # w初始值
a = 0.01  # 学习效率,每次
w_list = []  # 记录w变化
cost_list = []  # 记录损失变化

# 迭代修改w
for epoch in range(100):
    w_list.append(w)
    cost_list.append(cost(w, xs, ys))
    w -= a * gradient(w, xs, ys)
print(w_list)
print(cost_list)
plt.plot(np.asarray(w_list), np.asarray(cost_list))
plt.show()
