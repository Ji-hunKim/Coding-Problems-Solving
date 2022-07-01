from collections import deque

V, E, S = map(int, input().split())

graph = [[0] * (V + 1) for _ in range(V + 1)]

for _ in range(E):
  E1, E2 = map(int, input().split())
  # 노드 연결 하기
  graph[E1][E2] = graph[E2][E1] = 1

# 너비 우선 탐색
def bfs(start_node):
  discovered = [start_node]
  # 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(V)이다.
  # 그래서 시간복잡도가 O(1)인 deque를 사용한다.
  queue = deque() 
  queue.append(start_node)

  while queue:
    S = queue.popleft()
    print(S, end=' ')

    for w in range(len(graph[start_node])):
      if graph[S][w] == 1 and (w not in discovered):
        discovered.append(w)
        queue.append(w)

# 깊이 우선 탐색
def dfs(start_node, discovered=[]):
  discovered.append(start_node)
  print(start_node, end=' ')

  for w in range(len(graph[start_node])):
    if graph[start_node][w] == 1 and (w not in discovered):
      dfs(w, discovered)

dfs(S)
print()
bfs(S)