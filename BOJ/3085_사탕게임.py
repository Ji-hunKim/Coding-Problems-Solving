def check(a, s_row, e_row, s_col, e_col):
  n = len(a)
  result = 1

  #행 체크
  for i in range(s_row, e_row+1):
    cnt = 1
    for j in range(1, n):
      if a[i][j-1] == a[i][j]:
        cnt += 1
      else:
        cnt = 1
      if cnt > result:
        result = cnt
  
  #열 체크
  for i in range(s_col, e_col+1):
    cnt = 1
    for j in range(1, n):
      if a[j-1][i] == a[j][i]:
        cnt += 1
      else:
        cnt = 1
      if cnt > result:
        result = cnt
  return result


n = int(input())
a = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
  for j in range(n):
    if j < n-1:
      a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
      temp = check(a,i,i,j,j+1)
      if temp > result:
        result = temp
      a[i][j], a[i][j+1] = a[i][j+1], a[i][j]

    if i < n-1:
      a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
      temp = check(a,i,i+1,j,j)
      if temp > result:
        result = temp
      a[i][j], a[i+1][j] = a[i+1][j], a[i][j]

print(result)