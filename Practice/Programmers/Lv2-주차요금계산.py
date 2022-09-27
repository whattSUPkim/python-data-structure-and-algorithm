from datetime import timedelta
import math


def solution(fees, records):
    answer = list()
    records_by_car = dict()
    for record in records:
        a, b, c = record.split()
        try:
            records_by_car[b].append(a)
        except KeyError:
            records_by_car[b] = [a]

    for car in sorted(records_by_car.keys()):
        time_by_car = 0
        price_by_car = 0
        if len(records_by_car[car]) % 2 != 0:
            records_by_car[car].append("23:59")
        for r in range(0, len(records_by_car[car]), 2):
            i, o = records_by_car[car][r : r + 2]
            i_h, i_m = i.split(":")
            o_h, o_m = o.split(":")
            i = timedelta(hours=int(i_h), minutes=int(i_m))
            o = timedelta(hours=int(o_h), minutes=int(o_m))
            t = o - i
            time_by_car += t.total_seconds() / 60
        if time_by_car <= fees[0]:
            answer.append(fees[1])
        else:
            time_by_car -= fees[0]
            price_by_car += fees[1]
            price_by_car += math.ceil(time_by_car / fees[2]) * fees[3]
            answer.append(price_by_car)
    return answer
