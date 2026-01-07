#피드백: 재귀임은 알았으나, 탑타운방식으로 구현못했음..
def cmprs(arr,x,y,n):   
    for i in range(x, x+n):
        for j in range(y,y+n):
            if(arr[i][j] != arr[x][y]):
                n //= 2
                cmprs(arr,x,y,n)
                cmprs(arr,x+n,y,n)
                cmprs(arr,x,y+n,n)
                cmprs(arr,x+n,y+n,n)
                return
    answer[arr[x][y]] += 1      
    

def solution(arr):
    global answer
    answer = [0,0]
    cmprs(arr,0,0,len(arr))
    
    return answer