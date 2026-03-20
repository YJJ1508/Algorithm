def solution(n):
    #n의 1의 개수
    cnt_n = str(bin(n)[2:])
    cnt_n = cnt_n.count('1')
    
    result = 0
    #완전탐색
    num = n + 1 #다음 큰 수
    while True:
        #2진수 변환
        cnt_new = str(bin(num)[2:])
        cnt_new = cnt_new.count('1')
        #조건1,2 만족하는 경우 return
        if cnt_n == cnt_new:
            return num
        num += 1    
