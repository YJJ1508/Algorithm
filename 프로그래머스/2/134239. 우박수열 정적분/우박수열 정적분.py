def solution(k, ranges):
    area = []
    while k > 1: 
        prev_k = k  #현재값 저장 (윗변)
        #1.우박수열 계산 (아랫변)
        if k % 2 == 0: #짝수라면 2로 나눈다
            k //= 2
        else: #홀수라면 3을 곱하고 +1 
            k = k*3 + 1

        #2.넓이 저장 (사다리꼴)
        area.append((prev_k + k)/2)
            
    #3.ranges 범위 계산
    n = len(area)
    result = []
    for a,b in ranges:
        sum_area = sum(area[a:n+b]) if a<=n+b else -1
        result.append(float(sum_area))
    
    return result