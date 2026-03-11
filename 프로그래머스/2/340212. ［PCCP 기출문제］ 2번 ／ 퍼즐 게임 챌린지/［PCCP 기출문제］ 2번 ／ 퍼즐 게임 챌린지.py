def cal_times(diffs,times,limit,level):
    result = 0
    for i in range(len(diffs)):
        #diff <= level
        if diffs[i] <= level:
            result += times[i] 
        #diff > level
        else:
            result += (times[i]+times[i-1]) * (diffs[i]-level) + times[i]
    return result

def solution(diffs, times, limit):
    answer = 0 
    #이분탐색으로 level값을 선정
    start, end = min(diffs), max(diffs)
    while start <= end:
        mid = (start+end)//2
        #시간계산
        result = cal_times(diffs,times,limit,mid)
        #limit보다 작을때(만족), level값 더 작아져도 됨 
        if result <= limit:
            answer = mid  #값 기록
            end = mid - 1
        #limit 초과, level값이 더 커져야함
        else:  
            start = mid+1
    
    return answer