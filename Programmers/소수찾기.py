from itertools import permutations

def solution(numbers):
    answer = 0
    num = []
    
    for i in range(len(numbers)):
        a = list(permutations(numbers, i+1))
        num = num + a
    
    num2 = []
    for i in num:
        num2.append(int(''.join(k for k in i)))
    
    num2 = list(set(num2))
    
    for n in num2:
        cnt = 0
        sqrt =  int(n**0.5)
        if n == 1 or n == 0:
            continue
        for i in range(2, sqrt+1):
            if n % i == 0:
                cnt += 1
        if cnt == 0:
            answer += 1 
    return answer