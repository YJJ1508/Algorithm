# 첫시도: 35.7% 너무 복잡하게 구현했음
def solution(skill, skill_trees):
    
    count = 0
    for tree in skill_trees:
        #1. skill해당 단어만 남기기
        temp = ""
        for t in tree:  
            if t in skill:
                temp += t
        #2.count
        if skill[:len(temp)] == temp:
            count += 1
     
    return count