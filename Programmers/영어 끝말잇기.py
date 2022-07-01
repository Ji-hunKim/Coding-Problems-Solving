def solution(n, words):
    answer = []
    temp = []
    num = [i for i in range(1,n+1)]
    cnt, turn = 0, 0
    
    
    for word in words:
        cnt += 1
        if cnt % n == 1:
            turn += 1
        if len(temp) == 0:
            temp.append(word)
        else:
            if word[0] != temp[-1][-1] or word in temp:
                answer = [num[cnt%n-1], turn]
                return answer
            else:
                temp.append(word)
        
    return [0,0]