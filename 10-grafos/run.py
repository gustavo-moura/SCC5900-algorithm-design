import sys
data = sys.stdin.readlines()
content = [line.rstrip() for line in data]

from collections import deque


    
res = []
p = 0    

while True:
    n = int(content[p])
    # print(n)
    
    if n == 0:
        break
    
    p += 1
    m = int(content[p])
    # print(m)
    
    graph = [[0 for _ in range(n)] for _ in range(n)]
    
    color = [-1] * n
    
    for i in range(m):
        p += 1
        a,b = map(int, content[p].split())
        graph[a][b] = 1
        graph[b][a] = 1
        #print(a,b)
        
    p += 1
        
    q = deque([0])
    color[0] = 0
    flag = True
    
    while q:
        u = q.popleft()
        for v in range(n):
            if not graph[u][v]:
                continue
            
            if color[v] == -1:
                color[v] = color[u] + 1
                q.append(v)
                
            elif color[u] == color[v]:
                flag = False
                break
        
        if not flag:
            break
            
    if flag:
        print('BICOLORABLE.')
        res.append('BICOLORABLE.\n')
    else:
        print('NOT BICOLORABLE.')
        res.append('NOT BICOLORABLE.\n')