def solution(clothes):
    c = {}
    
    for clo in clothes:
        cl = clo[1]
        if cl not in c:
            c[cl] = 1
        else:
            c[cl] += 1
    answer = 1 
    
    for type in c: 
        answer *= (c[type] + 1)

    return answer-1