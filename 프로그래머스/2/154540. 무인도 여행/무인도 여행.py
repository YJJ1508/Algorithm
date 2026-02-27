from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(maps, a, b):
    r,c = len(maps), len(maps[0])
    result = int(maps[a][b])
    maps[a][b] = "X" #방문표시
    q = deque([(a,b)])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<r and 0<=ny<c and maps[nx][ny] != "X":
                result += int(maps[nx][ny])
                maps[nx][ny] = "X"
                q.append((nx,ny))
                
    return result

def solution(maps):
    maps = [list(r) for r in maps]
    r,c = len(maps), len(maps[0])
    
    answer = []
    #섬 도착 시작점 찾기
    for i in range(r):
        for j in range(c):
            if maps[i][j] != 'X':
                answer.append(bfs(maps, i, j))
                
    #머물 수 있는 무인도 없다면 -1
    if answer: return sorted(answer)
    else: return [-1]