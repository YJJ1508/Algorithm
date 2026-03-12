def solution(s):
    if len(s) == 1:
        return 1
    
    answer = len(s)
    #묶는 단위
    for size in range(1,len(s)//2 + 1):
        prev = s[0:size]
        count = 1
        compressed = ""
        
        #size단위로 문자열 확인
        for j in range(size,len(s),size):
            curr = s[j:j+size] #현재 마디
            if prev == curr:
                count += 1
            else:
                #지금까지 센 개수와 마디 합치기 2a 
                compressed += (str(count)+prev) if count >= 2 else prev
                prev = curr 
                count = 1
    
        #반복문 종료 후 남은 마지막 마디 처리
        compressed += (str(count) + prev) if count >= 2 else prev
        #최솟값 갱신
        answer = min(answer, len(compressed)) 
                
    return answer