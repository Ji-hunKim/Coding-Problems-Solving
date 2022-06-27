def solution(num): 
    new = []
    for number in num:
        new.append(str(number))
    new.sort(key = lambda x : x*3, reverse = True) 
    return ''.join(new)