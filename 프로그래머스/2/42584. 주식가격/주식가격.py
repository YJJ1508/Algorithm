#큐, 스택 둘 다 가능
from collections import deque

def solution(prices):
    answer = [] 
    prices = deque(prices) 
    
    #앞의값부터 초확인
    while prices:
        price = prices.popleft() 
        time = 0
        for p in prices:
            time += 1
            if price > p:
                break
        answer.append(time)
    
    return answer