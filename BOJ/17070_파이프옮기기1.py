n = int(input())
graph = [[] for _ in range(n)]

# 0은 가로, 1은 세로, 2는 대각선
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
# 그래프 정보 입력
for i in range(n):
    graph[i] = list(map(int, input().split()))

dp[0][0][1] = 1  # 첫 시작 위치

# dp를 위해서는 윗 행을 사용해야하므로 첫 행을 먼저 초기화
for x in range(2, n):
    if graph[0][x] == 0:
        dp[0][0][x] = dp[0][0][x - 1]

for i in range(1, n):
    for j in range(1, n):
        # 현재위치가 대각선인 경우
        if graph[i][j] == 0 and graph[i][j - 1] == 0 and graph[i - 1][j] == 0:
            dp[2][i][j] = dp[0][i - 1][j - 1] + dp[1][i - 1][j - 1] + dp[2][i - 1][j - 1]

        if graph[i][j] == 0:
            # 현재 위치가 가로인 경우
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            # 현재 위치가 세로인 경우
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]

print(sum(dp[i][n - 1][n - 1] for i in range(3)))