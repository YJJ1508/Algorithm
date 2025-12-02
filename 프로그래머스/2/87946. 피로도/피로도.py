import itertools
def solution(k, dungeons):
    answer = 0
    
    #모든 경우의 수 확인
    dungeons = list(itertools.permutations(dungeons))
    for i in dungeons: #[ [[80,20],[50,40],[30,10]] , [[80,20],[30,10],[50,40]] ] 
        count = 0
        temp_k = k
        for a,b in i:
            #최소 필요 피로도 만족 체크
            if a <= temp_k:
                temp_k -= b
                count += 1
        if count > answer:
            answer = count
    
    return answer