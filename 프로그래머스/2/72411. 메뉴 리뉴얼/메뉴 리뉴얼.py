from itertools import combinations
from collections import Counter

def combi(orders, n):
    combis = []
    #조합만들고 개수세기
    for order in orders:
        for c in combinations(sorted(order),n):
            combis.append("".join(c))
    counter = Counter(combis)
    
    #조합 없거나 빈도 2미만이면 빈 리스트 리턴
    if not counter or max(counter.values()) < 2:
        return []
    #가장 많이 나온 조합 리턴
    max_n = max(counter.values())
    return [k for k,v in counter.items() if v == max_n]
    
        
def solution(orders, course):
    result = []
    for i in course:
        result.extend(combi(orders,i))
    
    return sorted(result)