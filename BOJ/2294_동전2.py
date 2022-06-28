n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

dp = [0] + [100001 for _ in range(k)]

for i in arr:
    for j in range(i, k+1):
        dp[j] = min(dp[j-i]+1, dp[j])
if dp[k] != 100001:
    print(dp[k])
else:
    print(-1)
