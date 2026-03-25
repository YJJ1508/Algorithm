def solution(elements):
    nums = set()
    elem_2 = elements + elements 
    
    #완전탐색 
    for i in range(1,len(elements)+1): #길이 
        for j in range(len(elements)): #길이 i인 연속 부분 수열
            new = sum(elem_2[j:j+i])
            nums.add(new)
    
    return len(nums)
    

        