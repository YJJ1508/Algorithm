#알고리즘: 수학
#틀린이유: 시뮬로 풀었는데 규칙으로 풀어야하는문제다
import math
def solution(w,h):
    total = w*h
    #사용할 수 없는 사각형(가로+세로-최대공약수)
    cant_use = w+h - math.gcd(w,h)
    
    return total - cant_use
