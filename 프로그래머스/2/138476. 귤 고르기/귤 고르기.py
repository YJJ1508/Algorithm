from collections import Counter
def solution(k, tangerine):
    cnt_tan = Counter(tangerine) 

    #같은 개수가 많은순으로 정렬
    cnt_tan = sorted(cnt_tan.items(), key=lambda x:x[1], reverse=True)
    #개수 많은 순으로 차감
    idx = 0
    while k > 0:  
        k -= cnt_tan[idx][1]
        idx += 1
    
    return idx