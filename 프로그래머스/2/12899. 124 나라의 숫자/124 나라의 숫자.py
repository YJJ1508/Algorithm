#첫시도: 수열의 규칙(틀림) 
#3진법 변형원리로 풀기
def solution(n):
    num = ['1', '2', '4']
    answer = ''

    while n > 0:
        n -= 1 
        answer = num[n % 3] + answer 
        n //= 3

    return answer
