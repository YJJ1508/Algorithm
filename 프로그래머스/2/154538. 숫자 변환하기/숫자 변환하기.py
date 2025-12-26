#bfs 문제
from collections import deque
def solution(x, y, n):
    graph = [10001] * (y+1)
    
    #시작 인덱스 값 초기화
    graph[x] = 0
    q = deque()
    q.append(x) 
    
    while q:
        now = q.popleft()
        for i in [now+n, now*2, now*3]:
            if i > y:
                continue
            if graph[now] + 1 < graph[i]:
                graph[i] = graph[now] + 1
                q.append(i)   
    
    #결과 출력
    if graph[y] == 10001:
        return -1
    else:
        return graph[y]