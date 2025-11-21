def solution(elements): #[1,1,4,7,9]1           
    
    l = len(elements) #원래 길이
    elements = elements + elements #원형이라 더하기 위함
    
    num = set(elements) 
    for i in range(2,l+1): #길이(더할 숫자 개수) 2~5
        for j in range(0, l):  
            new = sum(elements[j:j+i])
            num.add(new)
            
    return len(num)