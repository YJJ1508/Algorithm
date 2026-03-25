def solution(n, words):
    check = [words[0]]
    #words 순회하며 틀린 단어 찾기
    for i in range(1,len(words)):
        #나온 단어인지 확인하기
        if words[i] not in check:
            check.append(words[i])
        else:
            return [i%n+1, i//n+1]
        
        #끝말잇기 틀린경우
        if words[i][0] != words[i-1][-1]:
            return [i%n+1, i//n+1]
    
    return [0,0]