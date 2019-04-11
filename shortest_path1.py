nodes = ('A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
distances = {
    'A':{'B':5,'C':6,'D':4,'E':7},
    'B':{'A':5,'F':2,'G':3},
    'C':{'A':6,'F':6,'G':4,'H':1},
    'D':{'A':4,'G':7,'H':3,'I':6},
    'E':{'A':7,'H':9,'I':1},
    'F':{'B':2,'C':6,'J':2,'K':3},
    'G':{'B':3,'C':4,'D':7,'J':6,'K':4,'L':1},
    'H':{'C':1,'D':3,'E':9,'K':7,'L':3,'M':6},
    'I':{'D':6,'E':1,'L':9,'M':7},
    'J':{'F':2,'G':6,'N':2,'O':3},
    'K': {'F': 3, 'G': 4, 'H': 7, 'N': 6, 'O': 4, 'P': 1},
    'L': {'G': 1, 'H': 3, 'I': 9, 'O': 7, 'P': 10, 'Q': 6},
    'M': {'H': 6, 'I': 7, 'P': 9, 'Q': 8},
    'N': {'J': 2, 'K': 6, 'R': 2, 'S': 3},
    'O': {'J': 3, 'K': 4, 'L': 7, 'R': 6, 'S': 4, 'T': 1},
    'P': {'K': 1, 'L': 10, 'M': 9, 'S': 7, 'T': 3, 'U': 6},
    'Q': {'L': 6, 'M': 8, 'T': 9, 'U': 1},
    'R': {'N': 2, 'O': 6, 'V': 2, 'W': 3},
    'S': {'N': 3, 'O': 4, 'P': 7, 'V': 6, 'W': 4, 'X': 1},
    'T': {'O': 1, 'P': 3, 'Q': 9, 'W': 7, 'X': 3, 'Y': 6},
    'U': {'P': 6, 'Q': 1, 'X': 9, 'Y': 1},
    'V': {'R': 2, 'S': 6, 'Z': 5},
    'W': {'R': 3, 'S': 4, 'T': 7, 'Z': 6},
    'X': {'S': 1, 'T': 3, 'U': 9, 'Z': 4},
    'Y': {'T': 6, 'U': 1, 'Z': 7},
    'Z': {'V': 5, 'W': 6, 'X': 4, 'Y': 7}
                    }

unvisited = {node: None for node in nodes} #把None作为无穷大使用
visited = {}#用来记录已经松弛过的数组
current = 'A' #要找A点到其他点的距离
currentDistance = 0
unvisited[current] = currentDistance#A到A的距离记为0

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue#被访问过了，跳出本次循环
        newDistance = currentDistance + distance#新的距离
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:#如果两个点之间的距离之前是无穷大或者新距离小于原来的距离
            unvisited[neighbour] = newDistance#更新距离
    visited[current] = currentDistance#这个点已经松弛过，记录
    del unvisited[current]#从未访问过的字典中将这个点删除
    if not unvisited: break#如果所有点都松弛过，跳出此次循环
    candidates = [node for node in unvisited.items() if node[1]]#找出目前还有拿些点未松弛过
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]#找出目前可以用来松弛的点
    if(current == "Z"):
        print('Start-End最短路径长度为:',currentDistance)
