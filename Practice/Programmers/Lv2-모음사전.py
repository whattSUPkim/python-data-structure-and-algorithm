def solution(word):
    idx = -1
    supporter = ""
    dic = dict()

    def dfs():
        nonlocal idx, supporter
        idx += 1
        dic[supporter] = idx
        if len(supporter) >= 5:
            return
        for c in "AEIOU":
            supporter += c
            dfs()
            supporter = supporter[:-1]

    dfs()
    return dic[word]
