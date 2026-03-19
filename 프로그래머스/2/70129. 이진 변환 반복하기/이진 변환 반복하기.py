def solution(s):
    zero, n = 0, 0    #제거할 0의 개수, 변환 횟수
    while len(s) > 1:
        #1. 0의 개수 count
        count_zero = s.count('0')
        zero += count_zero
        #2. x의 길이 c -> 4(c)를 2진법으로 표현
        c = len(s) - count_zero
        s = bin(c)[2:]

        n += 1
    
    return [n, zero]