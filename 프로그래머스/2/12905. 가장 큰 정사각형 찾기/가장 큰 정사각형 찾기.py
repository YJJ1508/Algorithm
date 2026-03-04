def solution(board):
    length = 0
    r, c = len(board), len(board[0])
    d = [[0]*(c+1) for _ in range(r+1)]
    
    for i in range(1,r+1):
        for j in range(1,c+1):
            if board[i-1][j-1]:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1])+1 
            length = max(length, d[i][j]) 

    return length**2