def solution(number, k):
    stack = []
    for n in number:
        #n보다 작은 앞 숫자는 다 지움
        while len(stack) > 0 and k > 0 and stack[-1] < n:
            stack.pop()
            k -= 1
        stack.append(n)
        
    if k:
        return number[:-k] #ex) 4321 내림차순 
    else:
        return "".join(stack)
    