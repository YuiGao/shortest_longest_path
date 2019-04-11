import copy

import networkx as nx  # 导入网络分析模块

import matplotlib.pyplot as plt  # 图形绘制模块


# 以下为求解最短路径

def findCloestrout(inf, rout, S, U, cloest_rout):
    key_UtoS = {}  # 记录u的每个key到D点会通过哪个已经确定的最短路径，用于后面输出最短路线

    for key in U:

        for key2 in S:

            if key + key2 in rout:

                if rout[key + key2] + S[key2] >= U[key]:  # 保持存储最大值

                    U[key] = rout[key + key2] + S[key2]

                    key_UtoS[key] = key2

            elif key2 + key in rout:

                if rout[key2 + key] + S[key2] >= U[key]:
                    U[key] = rout[key2 + key] + S[key2]

                    key_UtoS[key] = key2

            else:

                continue

    min_value = inf

    key_min = None

    for key in U:  # 找最大的路径

        if U[key] > min_value:
            min_value = U[key]

            key_min = key

    del U[key_min]  # 从未确定的最短路径集合删除可以确定的最短路径

    S[key_min] = min_value  # 添加已经确定的最短路径

    for num in range(len(cloest_rout)):

        if cloest_rout[num][-1] == key_UtoS[key_min]:
            temp_list = copy.deepcopy(cloest_rout[num])  # 这里一定要深拷贝，不然后一改全改

            temp_list.append(key_min)

            cloest_rout.append(temp_list)


# 以下为绘制带权值无向图

def draw(rout, rout_list):
    G = nx.Graph()  # 创建一个空图

    G.add_weighted_edges_from(rout_list)  # 添加权值边

    weight_list = {}

    for it in rout_list:  # 制作一个全权值表

        weight_list[it[0], it[1]] = it[2]

    pos = nx.spring_layout(G)  # 设置点的布局

    nx.draw_networkx_edge_labels(G, pos, weight_list, font_size=10)  # 绘制权值

    nx.draw(G, pos, node_color='g', edge_color='r', with_labels=True, \
 \
            font_color='b', font_size=20, node_size=800)  # 绘制权值边

    plt.show()  # 显示绘图
