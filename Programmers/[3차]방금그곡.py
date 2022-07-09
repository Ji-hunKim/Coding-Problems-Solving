def change(music):
    if 'A#' in music:
        music = music.replace('A#', 'a')
    if 'F#' in music:
        music = music.replace('F#', 'f')
    if 'C#' in music:
        music = music.replace('C#', 'c')
    if 'G#' in music:
        music = music.replace('G#', 'g')
    if 'D#' in music:
        music = music.replace('D#', 'd')   
    return music

def solution(m, musicinfos):
    answer = ''
    m = change(m)
    maxx = 0
    for info in musicinfos:
        start, end, song, melody = info.split(',')
        melody = change(melody)
        start = start.replace(':','')
        end = end.replace(':','')
        s1 = int(start[0:2])
        e1 = int(end[0:2])
        s2 = int(start[2:4])
        e2 = int(end[2:4])
        duration = (e1 - s1) * 60
        result = e2-s2
        if result < 0:
            result = result + 60
            duration -= 60
        duration += result
        i, k = 0, 0
        wm = []
        while k < duration:
            if i == len(melody)-1:
                wm.append(melody[i])
                i = -1
            else:
                wm.append(melody[i])
            k += 1
            i += 1
        
        final = ''.join(wm)
        if m in final:
            if maxx < duration:
                maxx = duration
                answer = ''
                answer += song
            if maxx == duration:
                continue
    if not answer:
        return "(None)"
    return answer