def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
            continue
        stack.append(s[i])
    
    if not stack: return 1
    else: return 0