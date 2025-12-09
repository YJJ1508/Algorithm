#틀린이유: (시간초과) n(for루프)+n(슬라이싱) = O(n^2) 
# counter  전체를 오른쪽으로 옮기면서 체크 = o(n)
from collections import Counter
def solution(topping):
    answer = 0
    left = Counter(topping) #전체를 왼쪽에 옮기기
    right = set()
    
    #토핑을 하나씩 오른쪽으로 옮기기
    for t in topping:
        #왼쪽 토핑 제거
        left[t] -= 1
        if left[t] == 0:
            left.pop(t) #해당 종류 더 없으면 제거
        #오른쪽에 옮기기
        right.add(t)
        #양쪽 공평한지 확인
        if len(left) == len(right):
            answer += 1 
        
    return answer