def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    one = []
    two = []
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            one.append(str1[i] + str1[i+1])
    for j in range(len(str2)-1):
        if str2[j].isalpha() and str2[j+1].isalpha():
            two.append(str2[j] + str2[j+1])
    

    temp = two.copy()
    h = two.copy()
    for i in one:
        if i in temp:
            temp.remove(i)
        else:
            h.append(i)
    
    temp = two.copy()
    g = []
    for i in one:
        if i in temp:
            g.append(i)
            temp.remove(i)

    if len(h) == 0:
        usa = 1
    else:
        usa = len(g) / len(h)
    return int(usa * 65536)