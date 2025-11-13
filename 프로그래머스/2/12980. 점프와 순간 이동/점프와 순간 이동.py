#[그리디 방식 문제] 
# 틀린이유: dp로 풀면 시간초과 n의 크기가 커서 안됨

def solution(n):  #5 -> 4(+1) 2 1 -> 0(+1)
    answer = 0
    while n > 0:
        #순간이동 가능한 경우
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
            answer += 1 #이동 수 +1
            
    return answer