def solution(n, k):
    answer = 0
    
    #k진수 변환
    trans_n = ""
    while n:
        trans_n += str(n % k)
        n = n // k
    trans_n = trans_n[::-1]
    
    #소수 판별
    trans_n = trans_n.split("0")
    for i in trans_n:
        isPrime = True
        #1이하거나 ''일때 패스
        if len(i) <= 0 or int(i) <= 1:
            continue
        #소수 판별
        for j in range(2,int(int(i)**0.5)+1):
            if int(i) % j == 0:
                isPrime = False
                break
        #소수라면 +1
        if isPrime:
            answer += 1
                
    
    return answer