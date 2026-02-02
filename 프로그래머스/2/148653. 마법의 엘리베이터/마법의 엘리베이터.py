#최초시도: BFS로 접근 -> 답봄
def solution(storey):
    answer = 0
    
    #일의 자리부터 0으로 처리
    while storey:
        r = storey % 10  #일의 자리
        #6~9
        if r > 5:
            answer += (10 - r) #16->20으로 만드는 셈
            storey += 10    #20올렸으니 십의자리 +1
        #0~4
        elif r < 5: #내리기
            answer += r 
        #5
        else:
            #다음 자릿수 5이상이면 올림
            if (storey // 10) % 10 > 4: 
                storey += 10
            answer += r
            
        storey //= 10
    
    return answer
    