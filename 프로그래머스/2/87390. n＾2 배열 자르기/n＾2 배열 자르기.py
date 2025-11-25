#틀린이유: 브루트포스 x (시간초과) => 규칙으로 푸는 문제

def solution(n, left, right):    #1 2 [3 2 2 3] 3 3 3  
    answer = []
    for i in range(left,right+1):
        a = i // n
        b = i % n
        answer.append(max(a,b)+1)
    return answer