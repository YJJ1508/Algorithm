def solution(land):
    
    #행돌기
    for i in range(1,len(land)):
        #열 돌기
        for j in range(4): 
            if j == 0:
                x,y,z = 1,2,3
            elif j == 1:
                x,y,z = 0,2,3
            elif j == 2:
                x,y,z = 0,1,3
            else:
                x,y,z = 0,1,2
            new1 = land[i][j] + land[i-1][x]
            new2 = land[i][j] + land[i-1][y]
            new3 = land[i][j] + land[i-1][z]
            land[i][j] = max(new1, new2, new3)

    return max(land[len(land)-1])