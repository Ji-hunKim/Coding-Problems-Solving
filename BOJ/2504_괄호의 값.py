instr = input()
stack = []
tmp = 1
result = 0

for i in range(len(instr)):
    if instr[i] == '(': 
        tmp *= 2
        stack.append(instr[i])
    elif instr[i] == '[':
        tmp *= 3
        stack.append(instr[i])

    elif instr[i] == ')':
        # 짝이 맞지 않는 경우이기 때문에 break 후 0 return
        if not stack or stack[-1] == '[': 
            result = 0
            break
        # 짝이 맞는 경우 + 이전값이 짝인 경우
        if instr[i-1] == '(':
            result += tmp
        tmp //= 2
        stack.pop() 

  
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        # 짝이 맞는 경우 + 이전 값이 짝인 경우
        if instr[i-1] == '[':
            result += tmp
        tmp //= 3
        stack.pop() 

if stack:
    result = 0
print(result)
    
