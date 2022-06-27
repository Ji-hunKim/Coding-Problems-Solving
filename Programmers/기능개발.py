import math

def solution(progresses, speeds):
    answer = [] 
    fin = 0
    cnt = 0
    
    for i in range(len(progresses)):
        pro = progresses[i]
        speed = speeds[i]
        left = 100 - pro
        
        if left - speed * cnt <= 0:
            fin += 1
        else:   
            cnt += math.ceil(left / speed) - cnt
            if i == 0:
                fin += 1
            else:
                answer.append(fin)
                fin = 1
        if i == len(progresses) - 1:
            answer.append(fin)
    return answer