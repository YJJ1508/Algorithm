from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(board,x,y):
    r, c = len(board), len(board[0])
    q = deque([(x,y,0)])
    visited = [[float('inf')]*c for _ in range(r)]
    visited[x][y] = 0
    
    while q:
        x,y,dist = q.popleft()  #출발지점(고정)
        
        #목표지점 도달한 경우 반환
        if board[x][y] == "G":
            return dist
        
        #방향 탐색
        for i in range(4):
            nx, ny = x, y   #현재지점(이동중)
            #1.해당 방향으로 미끄러지기
            while True:
                next_nx = nx + dx[i]    #다음 예상 위치
                next_ny = ny + dy[i]
                #이동 전, 범위 벗어나지 않고 장애물아니면 전진
                if 0<=next_nx<r and 0<=next_ny<c and board[next_nx][next_ny] != "D":
                    nx, ny = next_nx, next_ny
                else:
                    break 
            #2.방문한적 없거나, 더 짧은 경로 가능하면 갱신
            if visited[nx][ny] > dist + 1:
                visited[nx][ny] = dist + 1
                q.append((nx,ny,dist+1))
     
    #도달할 수 없는 경우
    return -1
    

def solution(board):
    #시작 점 찾기
    x, y = 0,0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                x, y = i,j
                break
                
    return bfs(board,x,y)
    