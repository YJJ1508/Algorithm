def convert(num, base):
    if num == 0:
        return "0"
    
    temp = "0123456789ABCDEF"
    result = ''
    while num > 0:
        result += temp[num % base]
        num //= base
    return result[::-1]
    
def solution(n, t, m, p):
    temp = ''
    for i in range(m*t):
        temp += str(convert(i,n))
    
    answer = '' 
    #튜브 순서 뽑아주기
    while len(answer) < t:
        answer += temp[p-1]
        p += m

    return answer