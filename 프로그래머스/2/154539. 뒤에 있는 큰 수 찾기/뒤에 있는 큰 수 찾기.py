#단순구현:89.2%(x) 스택구조 문제 
def solution(numbers): 
    
    answer = [-1] * len(numbers) #-1로 초기화: 없을 경우 -1
    stack = [] #큰수 찾을 "인덱스" 담기
    
    for i in range(len(numbers)): #i인덱스 => 큰수
        #큰수 찾기
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i] #큰수 기록하기
        stack.append(i) #찾을 대상 넣기
    
    return answer 