from collections import Counter

def solution(s):
    answer = []    
    tmp = ""
    num = []

    for i in range(len(s)-2):
        if s[i].isdigit():
            tmp += s[i]
        if s[i+1] == ',' and s[i+2].isdigit() or s[i+1] == '}':
            num.append(int(tmp))
            tmp = ""

    for d, c in Counter(num).most_common():
        answer.append(d)
        
    return answer