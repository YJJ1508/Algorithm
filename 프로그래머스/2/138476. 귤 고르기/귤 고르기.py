def solution(k, tan): #다른 종류 최소화
    result = 0
    
    #각 숫자 개수 담아주기
    dp = [0] * (max(tan) + 1)
    for i in tan:
        dp[i] += 1
    #개수가 많은것부터 담기
    dp.sort(reverse = True) #오름차순 [5: 2 3: 2 3: 2]
    #k개 만큼 담아주기 
    for i in dp:
        if k <= 0:
            break
        k -= i
        result += 1 #종류 카운트
    
    return result