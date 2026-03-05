def hanoi(n,start,mid,end,answer):
    if n == 1: #종료조건
        answer.append([start,end])
        return answer
    
    #n-1개 원반을 출발지 -> 보조 기둥
    hanoi(n-1, start,end,mid,answer)
    #가장 큰 원반을 출발지 -> 목적지
    answer.append([start,end])
    #n-1개 보조기둥 원반 -> 목적지
    hanoi(n-1,mid,start,end,answer)
    return answer

def solution(n):
    answer = []
    return hanoi(n,1,2,3,answer)