#틀린이유: 선을 칸으로 치환할수 있다 생각했으나 x(모호함)
#(0,0) (0,1) 같은길인데 다른길로 처리됨. (구조적으로 안맞음)
from collections import deque
def solution(dirs):
    move = {'U': (0,1), 'D': (0,-1), "L": (-1,0), "R": (1,0)}
    answer = set()
    x,y = 0,0
    #cmd대로 좌표 이동
    for cmd in dirs:
        dx, dy = move[cmd]
        nx = x + int(dx)
        ny = y + int(dy)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            answer.add((x,y,nx,ny)) #출발도착 == 도착출발 
            answer.add((nx,ny,x,y)) #도착출발
            x,y = nx, ny
    
    return len(answer) // 2     #길 두번 넣은거 제거