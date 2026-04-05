def solution(citations):
    result = 0
    
    l = 0
    r = len(citations)
    while l <= r:
        mid = (l+r)//2
        
        check = 0 
        #h-index 조건확인
        for num in citations:
            if num >= mid:
                check += 1
        #범위탐색
        if mid <= check:
            result = mid
            l = mid + 1  #mid수가 커져야함      
        else: 
            r = mid - 1  #mid수가 작아져야함
            
    return result
            
            