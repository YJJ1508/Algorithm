def solution(n, words):  #먼저 탈락하는 사람 번호, 몇번째 차례에 탈락
    answer = [0,0]

    temp = [words[0][0]] 
    round = 0
    for i in range(n-1,len(words), n): #각 라운드마다 끊기
        round += 1
        for j in range(i+1-n,i+1): # 각 라운드의 단어 순회
            #통과
            if words[j] not in temp and temp[-1][-1] == words[j][0] :
                temp.append(words[j])
            #탈락하는 경우
            else:
                num = (j+1) % n #1//2     
                answer[0] = n if num == 0 else num #탈락 번호
                answer[1] = round #탈락 라운드 
                return answer
                
    return answer