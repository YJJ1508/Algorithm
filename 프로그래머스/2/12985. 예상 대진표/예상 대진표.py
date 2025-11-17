#반으로 계속 줄이는 과정 - 같아지는 순간 같은 그룹 (같은 노드찾기)
def solution(n,a,b):    # 12 34 56 78 
    answer = 0         #1 11 22 33 44  
                             
    while a != b:
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
   
    return answer