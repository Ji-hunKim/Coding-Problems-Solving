n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

maxx = -1000000001
minn = 1000000001

def dfs(cnt, result, add, sub, mul, div):
    global maxx
    global minn
    if cnt == n:
        maxx = max(maxx, result)
        minn = min(minn, result)
        return
    if add > 0:
        dfs(cnt + 1, result + num[cnt], add-1, sub, mul, div)
    if sub > 0:
        dfs(cnt + 1, result - num[cnt], add, sub-1, mul, div)
    if mul > 0:
        dfs(cnt + 1, result * num[cnt], add, sub, mul-1, div)
    if div > 0:
        dfs(cnt + 1, -((-result) // (num[cnt])) if result < 0 else result // num[cnt] , add, sub, mul, div-1)
 
dfs(1, num[0], add, sub, mul, div)

print(maxx)
print(minn)