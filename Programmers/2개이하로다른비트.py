def bin_to_dex(n): 
    return int('0b' + ''.join(n), 2)

def solution(numbers):
    answer = []
    for num in numbers:
        change = False
        num = list(bin(num)[2:])
        l = len(num)
        for i in range(l-1, -1, -1):
            if num[i] == '0':
                if i == l-1:
                    num[i] = '1'
                    answer.append(bin_to_dex(num))
                    change = True
                    break
                else:
                    num[i] = '1'
                    num[i+1] = '0'
                    answer.append(bin_to_dex(num))
                    change = True
                    break
        if change == False:
            num.insert(0,'1')
            num[1] = '0'
            answer.append(bin_to_dex(num))
    return answer