def solution(n,a,b):
    answer = 0
    #매 라운드 반씩 줄어듦
    while a != b: #같은 그룹일때 return
        a = (a+1)//2
        b = (b+1)//2
        answer += 1
        
    return answer