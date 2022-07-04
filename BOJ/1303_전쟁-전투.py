# DFS
n, m = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y,color):
  global cnt
  if x < 0 or x >= m or y < 0 or y >= n:
    return cnt
  
  if graph[x][y] == color:
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      cnt = dfs(nx, ny, color)
    return cnt
  return cnt

cnt = 0

w_count = 0
b_count = 0

for i in range(m):
  for j in range(n):  
    if graph[i][j] == 'W':
      w_count += dfs(i,j,'W') ** 2
      cnt = 0
    elif graph[i][j] == 'B':
      b_count += dfs(i,j,'B') ** 2
      cnt = 0

print(w_count,b_count)  


# BFS
from collections import deque
n, m = map(int, input().split())

graph = []
for i in range(m):
    graph.append(list(input()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(graph, x, y, color):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == color:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt

cnt = 0

w_count = 0
b_count = 0

for i in range(m):
  for j in range(n):  
    if graph[i][j] == 'W':
      w_count += bfs(graph,i,j,'W') ** 2
      cnt = 0
    elif graph[i][j] == 'B':
      b_count += bfs(graph,i,j,'B') ** 2
      cnt = 0

print(w_count,b_count)  