def solution(n):
    nums = ['4', '1', '2']
    answer = ''
    while n:
        answer += nums[n % 3]
        if n % 3 == 0:
            n -= 1
        n = n // 3
    return answer[::-1]