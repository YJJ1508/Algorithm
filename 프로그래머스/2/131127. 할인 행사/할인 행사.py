from collections import Counter
def solution(want, number, discount):
    count = 0
    s_n = sum(number) #구해야하는 과일의 총 개수
    want_n = {} #{'banana': 3, 'apple': 2, 'rice': 2}
    for i in range(len(want)):
        want_n[want[i]] = number[i]
    
    #discount 순회
    for i in range(len(discount)- s_n + 1): 
        counter = Counter(discount[i:i+s_n])
        #원하는 물품 모두 구매 가능한 경우
        if counter == want_n:
            count += 1
    
    return count
        
    