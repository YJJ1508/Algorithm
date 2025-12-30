def solution(order):
    count = 0
    
    stack = [] 
    idx = 0
    for box in range(1, len(order)+1):
        stack.append(box) #1
        while stack and stack[-1] == order[idx]:
            idx += 1
            stack.pop()
            count += 1
    
    return count