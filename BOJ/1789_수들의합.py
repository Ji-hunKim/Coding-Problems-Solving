n = int(input())
result = 0
cnt = 0

if n == 1 or n == 2:
  result = 1
else:  
  for i in range(1, n):
    n = n - i
    if n == 0 :
      result = i
      break
    elif n < 0:
      result = i - 1
      break

print(result)