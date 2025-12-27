import math 

def to_min(t):
    h, m = map(int, t.split(":"))
    return h * 60 + m

def calc_time(times):
    total = 0
    for i in range(0, len(times), 2):
        total += times[i+1] - times[i]
    return total

def calc_price(fees, time):
    price = fees[1]
    #기본 시간보다 낮은 경우 기본요금만 낸다
    if time <= fees[0]:
        return price
    price += math.ceil((time - fees[0]) / fees[2]) * fees[3]
    return price

def solution(fees, records):
    answer = []
    
    #1. 차량별 누적시간 뽑기
    #차량별로 묶기
    n_r = {}
    for i in records:
        time, num, inout = i.split()
        if num not in n_r:
            n_r[num] = [time]
        else:
            n_r[num].append(time)
    n_r = dict(sorted(n_r.items()))
    
    #차량별 주차 시간 뽑기
    total_time = [] #각 차량의 주차 시간 담기
    for num,values in n_r.items():
        n = len(values)
        #출차 안한 경우 추가
        if n % 2 != 0: 
            n_r[num].append("23:59") 
        #분으로 환산
        time = [] 
        for t in values:
            time.append(to_min(t))
        total_time.append(calc_time(time))
    
    #2. 차량별 주차 요금 계산 
    price = []
    for i in total_time:
        price.append(calc_price(fees,i))
 
    return price
    
    
