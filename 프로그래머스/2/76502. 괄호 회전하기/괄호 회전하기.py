def solution(s):   
    count = 0
    
    temp = ''
    result = []
    for i in range(len(s)):
        #1. s를 x칸만큼 회전
        temp = s[i:len(s)+1]+s[0:i]  
        #2. 올바른 괄호 문자열인지 확인
        stack = []
        check = True   
        for j in temp:
            if not stack:
                if j == '}' or j ==']' or j==')':
                    check = False
                    break
                stack.append(j)
            else:
                if j == '{' or j=='(' or j=="[":
                    stack.append(j)
                else:
                    if stack[-1]=="{" and j =="}":
                        stack.pop()
                    elif stack[-1]=="[" and j==']':
                        stack.pop()
                    elif stack[-1]=='(' and j==')':
                        stack.pop()
        #올바른 괄호 문자열 +1
        if not stack and check == True:
            count += 1 
        
    return count