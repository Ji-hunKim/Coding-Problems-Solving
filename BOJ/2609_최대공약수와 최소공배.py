a, b = map(int, input().split())

maxx = max(a,b)
minn = min(a,b)

originmax = maxx
originmin = minn

divide = []

for i in range(minn, 1, -1):
    if maxx % i == 0 and minn % i == 0:
        maxx = maxx/i
        minn = minn/i
        divide.append(i)

if originmax == maxx:
    print(1, maxx * minn)
else:
    one = 1
    for d in divide:
        one *= d
    print(one, int(one * maxx * minn))

