def solution(n):
    arr = [[0]*i for i in range(1,n+1)] #[[0], [0,0], [0,0,0]]
    
    x, y = -1, 0 #시작위치
    num = 1 
    for i in range(n): #(아래 -> 오른쪽 -> 위 -> 아래)
        for j in range(i,n): #(ex.아래에서 각 지점 1,2,3,4 접근)
            #아래
            if i % 3 == 0:
                x += 1
            #오른쪽
            elif i % 3 == 1:
                y += 1
            #대각선 위
            else:
                x -= 1
                y -= 1
            
            arr[x][y] = num #숫자 기록
            num += 1
    
    return [val for row in arr for val in row]