#틀린이유: 완전탐색시 시간초과, 규칙으로 풀어야함
def solution(n, left, right):
    arr = []
    for i in range(left, right+1):
        a = i//n
        b = i%n
        arr.append(max(a,b)+1)
         
    return arr