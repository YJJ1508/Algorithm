import math
def gcd(a,b):
    return math.gcd(a,b)

def is_divided(array,x):
    for i in array:
        if i % x == 0:
            return 0
    return 1

def solution(arrayA, arrayB):
    answer = 0
    
    #arrayA gcd 
    r1 = arrayA[0]
    for i in range(0,len(arrayA)-1):
        r1 = gcd(r1,arrayA[i+1])
    #arrayB gcd
    r2 = arrayB[0]                             
    for i in range(0,len(arrayB)-1):
        r2 = gcd(r2,arrayB[i+1])                
                                                
    #상대 카드 나눠지지 않는지 확인
    if is_divided(arrayA,r2) == 0: r2 = 1
    if is_divided(arrayB,r1) == 0: r1 = 1
    
    #답 반환
    if r1 == 1 and r2 == 1: return 0
    else: return max(r1,r2)
            
        
    
    
    return answer