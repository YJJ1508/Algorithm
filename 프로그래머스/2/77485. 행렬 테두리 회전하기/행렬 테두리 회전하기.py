import copy
from collections import deque
def recursion(graph,x1,y1,x2,y2): #(2,2,5,4)
    nx,ny,currv = x1,y1,graph[x1][y1]  #현재 좌표
    mini = currv
    
    #오른쪽 이동
    for _ in range(y2-y1):
        ny += 1
        nextv = graph[nx][ny] 
        graph[nx][ny] = currv
        mini = min(mini, currv)
        currv = nextv
        
    #아래로 이동
    for _ in range(x2-x1):
        nx += 1
        nextv = graph[nx][ny] 
        graph[nx][ny] = currv
        mini = min(mini, currv)
        currv = nextv
    #왼쪽 이동
    for _ in range(y2-y1):
        ny -= 1
        nextv = graph[nx][ny] 
        graph[nx][ny] = currv
        mini = min(mini, currv)
        currv = nextv
    #위로 이동
    for _ in range(x2-x1):
        nx -= 1
        nextv = graph[nx][ny] 
        graph[nx][ny] = currv
        mini = min(mini, currv)
        currv = nextv

    return mini
        

def solution(rows, columns, queries):
    #그래프 초기화
    graph = [[0]*(columns+1) for _ in range(rows+1)]
    num = 1
    for i in range(1,rows+1):
        for j in range(1,columns+1):
            graph[i][j] = num
            num += 1
    
    #queries수행
    result = []
    cnt = 1
    for a,b,x,y in queries:
        result.append(recursion(graph, a,b,x,y))
        
    return result