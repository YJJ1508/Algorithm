#첫시도: 시간초과(매번 sum -> 최초에만, -1 예외처리 *2추가-> +2)
from collections import deque
def solution(queue1, queue2):
    #큐로 변환
    queue1,queue2 = deque(queue1), deque(queue2)
    #합 계산
    sum1, sum2 = sum(queue1), sum(queue2)
    
    #값 비교로 큰쪽값 pop&insert
    n = 0
    while sum1 != sum2:
        #예외처리
        if n > (len(queue1) + len(queue2))+2:
            return -1
        
        #양쪽 값 비교 후 pop&insert
        if sum1 > sum2:
            e = queue1.popleft()
            sum1 -= e
            queue2.append(e)
            sum2 += e
        else:
            e = queue2.popleft()
            sum2 -= e
            queue1.append(e)
            sum1 += e
            
        n += 1
    
    return n