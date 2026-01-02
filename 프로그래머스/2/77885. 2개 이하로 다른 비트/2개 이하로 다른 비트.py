#완전탐색으론 안되고 규칙 찾는 문제..

def f(x):
    #1.짝수일 경우 끝자리 +1
    if x % 2 == 0:
        return x+1
    
    #2.홀수일 경우
    else:
        b_x = bin(x)[2:]   
        #0이 섞여있는지 확인
        idx = 0
        for i in range(len(b_x)-1, -1, -1):
            if b_x[i] != '1':
                idx = i
                break
        #2-1. 모든 원소 1일때
        if idx == 0:
            b_x = '10' + b_x[1:]  #'10'+ 맨앞비트 제외 나머지
            return int(b_x, 2)
        #2-2. 0,1 혼합
        else:
            #마지막 01 -> 10으로
            b_x = b_x[:idx] + '10' + b_x[idx+2:] #
            return int(b_x, 2)

def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(f(i))
    
    return answer