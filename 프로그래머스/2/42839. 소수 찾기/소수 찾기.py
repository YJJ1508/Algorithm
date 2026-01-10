from itertools import permutations
def solution(numbers):
    new = []
    #1.모든 숫자 뽑아내기 
    temp = []
    for i in range(1,len(numbers)+1):
        temp.extend(permutations(numbers,i)) 
        new = [int(''.join(i)) for i in temp]
    new = list(set(new))

    #2.소수 찾기
    answer = 0
    for num in new:   
        if num < 2:
            continue
            
        check = True   
        for j in range(2,int(num**0.5)+1):
            if num % j == 0:
                check = False
                break
        if check: 
            answer += 1
            
    
    return answer