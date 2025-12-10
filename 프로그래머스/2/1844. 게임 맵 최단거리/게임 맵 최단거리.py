from collections import deque
def solution(maps): 
    answer = 0
    
    n = len(maps) #행
    m = len(maps[0]) #열
    visited = [[0]*m for _ in range(n)]
    visited[0][0] = 1
    maps[0][0] = 0 #방문표시
    q = deque()
    q.append((0,0))
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    #최단거리 세기
    while q:
        x, y = q.popleft() #현재 위치
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #영역 벗어나는 경우 제외 
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #방문하지 않았을 경우 최단거리 기록
            if maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1 #방문순서 기록
                maps[nx][ny] = 0 #방문 표시
                q.append((nx,ny)) #큐에 쌓기
    
    #도달할수 없는 경우
    if visited[n-1][m-1] == 0:  return -1
    else: return visited[n-1][m-1]
