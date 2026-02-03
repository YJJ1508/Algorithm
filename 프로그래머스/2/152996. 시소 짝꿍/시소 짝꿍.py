from collections import Counter
def solution(weights):
    answer = 0
    
    #1:1 
    counter = Counter(weights)
    for k,v in counter.items():
        if v >= 2:  #1:1 경우
            answer += v*(v-1) // 2
    weights = set(weights)  #계산 후 중복 없애주기
    
    #2:3, 2:4, 3:4 
    for w in weights:
        if w*2/3 in weights:
            answer += counter[w*2/3] * counter[w]
        if w*2/4 in weights:
            answer += counter[w*2/4] * counter[w]
        if w*3/4 in weights:
            answer += counter[w*3/4] * counter[w]
    
    return answer
    