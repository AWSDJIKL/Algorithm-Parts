def eggs(m, floors):
    """
    用m个鸡蛋确定最低几楼会摔碎，返回最坏情况下所需次数
    递归版，简单直接，但是时间复杂度很高，跑不出结果

    :param m: 鸡蛋个数
    :param floors: 一共多少层
    :return: 最坏情况下所需次数
    """
    # 只剩一个鸡蛋了，最坏情况需要从1层到floors层全部试一次
    if m == 1:
        return floors
    if floors <= 0 or m < 1:
        return 0
    min_k = floors
    # 测试不同的步长
    for k in range(1, floors):
        # 若第k层蛋没有碎，剩余需要测试的楼层就只有floors到k+1了，把k+1看作1，则floors=floors-k
        r1 = eggs(m, floors - k)
        # 若第k层蛋碎了，则需要测试1到k-1层
        r2 = eggs(m - 1, k - 1)
        result = max(r1, r2) + 1
        if min_k > result:
            min_k = result
    # 从2种情况中取最大值，模拟最坏情况
    return min_k


def eggs_cycle(m, floors):
    """
    循环版，比递归版更快得出结果

    :param m:鸡蛋个数
    :param floors:楼层高度
    :return:所需次数
    """
    # 低于1层或没有鸡蛋都无需尝试
    if floors < 1 and m < 1:
        return 0
    # 用二维数组f[鸡蛋个数][楼层高度]记录鸡蛋个数与楼层高度所对应的所需次数
    f = [[i for i in range(floors + 1)] for j in range(m + 1)]
    # 循环遍历更新不同鸡蛋个数，不同楼层高度时对应的次数，鸡蛋个数为1的不用更新，因为只能一个个试
    for m_i in range(2, m + 1):
        # 楼层从1层到最高层
        for floors_j in range(1, floors + 1):
            # 测试不同间隔所需次数，从中取最小值
            for k in range(1, floors_j):
                # 鸡蛋没碎
                r1 = f[m_i][floors_j - k] + 1
                # 鸡蛋碎了
                r2 = f[m_i - 1][k - 1] + 1
                # 最坏情况，二者取最大值
                result = max(r1, r2)
                # 更新结果
                f[m_i][floors_j] = min(f[m_i][floors_j], result)
    return f[m][floors]


def eggs_cycle_low_space(m, floors):
    """
    空间优化版

    :param m: 鸡蛋个数
    :param floors: 楼层高度
    :return: 最少所需次数
    """
    # 低于1层或没有鸡蛋都无需尝试
    if floors < 1 and m < 1:
        return 0
    # 用2个一维数组保存所需次数，f_pre代表m_i-1个鸡蛋在对应楼层数时所需的次数，f_cur代表m_i个鸡蛋在对应楼层数时所需的次数
    f_pre = [i for i in range(floors + 1)]
    f_cur = [i for i in range(floors + 1)]
    # 循环遍历更新不同鸡蛋个数，不同楼层高度时对应的次数，鸡蛋个数为1的不用更新，因为只能一个个试
    for m_i in range(2, m + 1):
        # 楼层从1层到最高层
        for floors_j in range(1, floors + 1):
            # 测试不同间隔所需次数，从中取最小值
            for k in range(1, floors_j):
                # 鸡蛋没碎，所以鸡蛋数量不变，还是m_i个，取f_cur中的次数
                r1 = f_cur[floors_j - k] + 1
                # 鸡蛋碎了，鸡蛋少一个，是m_i-1个，取f_pre中的次数
                r2 = f_pre[k - 1] + 1
                # 最坏情况，二者取最大值
                result = max(r1, r2)
                # 更新结果
                f_cur[floors_j] = min(f_cur[floors_j], result)
        # 保留m_i个鸡蛋时所需的次数
        f_pre = f_cur[:]
    return f_cur[floors]


# print(eggs(2, 100))
# print(eggs_cycle(2, 100))
print(eggs_cycle_low_space(2, 100))
