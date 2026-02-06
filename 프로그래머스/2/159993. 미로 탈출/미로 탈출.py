#틀린이유: s -> l   l -> e 로 접근했어야함 (s->e접근x)
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(maps, x, y, target):
    r, c = len(maps), len(maps[0])
    
    visited = [[-1]*c for _ in range(r)]
    q = deque([(x,y)])
    visited[x][y] = 0
    
    while q:
        x, y = q.popleft()
        
        #목표 지점(l or e)도달하면 거리 반환
        if maps[x][y] == target:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            #방문하지 않은 이동 가능 노드
            if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                
    return None
                
    
def solution(maps):
    x, y = 0,0
    x2,y2 = 0,0
    maps = [list(row) for row in maps]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                x, y = i, j
            if maps[i][j] == 'L':
                x2,y2 = i, j
    
    #1단계: S -> L 
    to_lever = bfs(maps, x, y, 'L')
    if to_lever is None:
        return -1
    #2단계: L -> E
    to_exit = bfs(maps, x2, y2, 'E')
    if to_exit is None:
        return -1
    
    #정답반환
    return to_lever + to_exit
        