n = int(input())
arr = list(map(int, input().split()))
sosu = []

for a in arr:
    if a == 1:
        continue
    if a == 2:
        sosu.append(a)
        continue
    for i in range(2, a//2+1):
        if a % i == 0:
            break
    else:
        sosu.append(a)

print(len(sosu))