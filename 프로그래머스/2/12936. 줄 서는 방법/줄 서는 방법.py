#완전탐색(permutations)대신 규칙으로 푸는 문제
import math
def solution(n, k):    
    answer = []
    number = [i for i in range(1, n+1)]
    
    #맨 앞자리에 올 숫자 하나씩 계산
    while number:
        perm = math.factorial(n-1) #현재 자리수의 순열 개수
        idx = (k-1) // perm    #k번째가 몇번째 묶음에 있는지
        answer.append(number.pop(idx)) #계산된 인덱스의 숫자 꺼내서 정답에 넣기 
        k %= perm #다음 자릿수 위해 k업데이트
        n -= 1 #n 줄여 다음 자리로 이동
    
    return answer