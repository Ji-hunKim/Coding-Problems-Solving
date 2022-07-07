def solution(files):
    answer = []
    real = []
    for j in range(len(files)):
        s = ''
        tmp = []
        file = files[j]
        H = False
        for i in range(len(file)):
            f = file[i]
            if H == False:
                if f.isnumeric() == False:
                    if f.isalpha():
                        s += f.lower()
                    else:
                        s += f
                else:
                    tmp.append(s)
                    s = ''
                    H = True
            if H == True:
                if f.isnumeric() == True:
                    s += f
                    if i == len(file)-1:
                        tmp.append(int(s))
                        break
                else:
                    tmp.append(int(s))
                    break
        tmp.append(j)
        answer.append(tmp)
    answer = sorted(answer, key = lambda x : (x[0], x[1]))
    for an in answer:
        real.append(files[an[2]])
    return real