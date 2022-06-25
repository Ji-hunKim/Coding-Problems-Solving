def solution(record):
    answer = []
    idic = {}
    for re in record:
        relist = re.split()
        cmd = relist[0]
        if cmd == 'Enter' or cmd == 'Change':
            idd = relist[1]
            nick = relist[2]
            idic[idd] = nick
    for re in record:
        relist = re.split()
        cmd = relist[0]
        if cmd == 'Enter':
            idd = relist[1]
            answer.append(idic[idd] + '님이 들어왔습니다.')
        elif cmd == 'Leave':
            idd = relist[1]
            answer.append(idic[idd] + '님이 나갔습니다.')
    return answer