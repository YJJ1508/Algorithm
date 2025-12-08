from collections import deque
def solution(priorities, location):
    answer = 0
    
    q = deque()
    for i in range(len(priorities)):
        q.append((i,priorities[i]))
    
    order = [] 
    while q:
        k, v = q.popleft()
        #우선순위 높은 인자 있는지 체크
        check = False 
        for k2,v2 in q:
            if v < v2:
                q.append((k,v)) #다시 넣기
                check = True
                break
        #우선순위 꺼내서 order에 넣기
        if check == False:
            order.append(k)
            
                
    return order.index(location) + 1