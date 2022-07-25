def solution(id_list, report, k):
    result = {key: 0 for key in id_list}
    d = {key: 0 for key in id_list}

    for r in set(report):
        _, b = r.split()
        d[b] += 1
    stopped_id = [name for name in d.keys() if d[name] >= k]

    for r in set(report):
        a, b = r.split()
        if b in stopped_id:
            result[a] += 1

    return [result[name] for name in id_list]

