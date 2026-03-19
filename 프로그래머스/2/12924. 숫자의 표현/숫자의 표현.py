def solution(n):
    s, e = 1,1
    answer = 0
    amount = s
    while s <= n:
        if amount < n:
            e += 1
            amount += e
        elif amount == n:
            answer += 1
            e += 1
            amount += e
        else:
            amount -= s
            s += 1
    
    return answer