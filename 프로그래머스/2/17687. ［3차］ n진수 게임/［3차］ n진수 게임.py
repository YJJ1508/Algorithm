def convert(num, base):
    temp = "0123456789ABCDEF"
    q, r = divmod(num, base) #몫, 나머지
    
    #더 이상 나눌 몫이 없으면 나머지 반환, 재귀적으로 나머지 합치기
    if q == 0:  
        return temp[r] 
    else:
        return convert(q,base) + temp[r]
    
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