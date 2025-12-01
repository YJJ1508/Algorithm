def solution(clothes):
    
    #종류별로 구분하기
    dic = {}
    for v,t in clothes:
        if t not in dic:
            dic[t] = [v] #리스트로 초기화
        else:
            dic[t].append(v)
    
        
    #조합 카운트
    answer = 1
    for _, t in dic.items():
        answer *= (len(t) + 1)
    
    
    return answer - 1