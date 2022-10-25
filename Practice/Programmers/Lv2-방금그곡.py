# https://school.programmers.co.kr/learn/courses/30/lessons/17683#
from datetime import timedelta


def solution(m, musicinfos):
    codes = "C, C#, D, D#, E, F, F#, G, G#, A, A#, B".split(",")
    new_codes = "HIJKLMNOPQRS"
    new_codes = {codes[i].strip(): new_codes[i] for i in range(len(codes))}
    for c in reversed(codes):
        c = c.strip()
        m = m.replace(c, new_codes[c])
    idx = 0
    answer = []
    for musicinfo in musicinfos:
        idx += 1
        t1, t2, name, code = musicinfo.split(",")
        t1 = timedelta(hours=int(t1[:2]), minutes=int(t1[3:]))
        t2 = timedelta(hours=int(t2[:2]), minutes=int(t2[3:]))
        t = int((t2 - t1).total_seconds() // 60)
        for c in reversed(codes):
            c = c.strip()
            code = code.replace(c, new_codes[c])
        code *= (t // len(code)) + 1
        if m in code[:t]:
            answer.append([name, t, idx])

    if answer:
        return max(answer, key=lambda x: (x[1], -x[2]))[0]
    else:
        return "(None)"

