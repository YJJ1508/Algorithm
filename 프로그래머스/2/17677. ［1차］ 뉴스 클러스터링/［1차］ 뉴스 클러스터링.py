#단순 구현  84.6%(2개x)
from collections import Counter
def solution(str1, str2):
    
    #1.두 글자씩 집합 만들기
    val = "abcdefghijklmnopqrstuvwxyz"
    #str1: 두 글자씩 집합으로 만들기
    n_str1 = []
    for s in range(len(str1)-1):
        #유효한 문자쌍인지 확인
        if str1[s].lower() in val and str1[s+1].lower() in val:
            n_str1.append(str1[s:s+2].upper())
    #str2: 두 글자씩 집합 만들기
    n_str2 = []
    for s in range(len(str2)-1):
        #유효한 문자쌍인지 확인
        if str2[s].lower() in val and str2[s+1].lower() in val:
            n_str2.append(str2[s:s+2].upper())

    #2.교집합 구현(중복 o)
    comm = 0
    temp2 = n_str2[::]
    for s in n_str1:
        if s in temp2:
            comm += 1
            idx = temp2.index(s)
            temp2.pop(idx)        
    #3.합집합 구현
    c_1 = Counter(n_str1)
    c_2 = Counter(n_str2)   
    minus = c_1 - c_2
    temp = minus + c_2
    add = sum(temp.values())

    #4.자카드 유사도
    if not comm and not add :
        return 65536
    else:
        answer = comm / add * 65536
        return int(answer)
    