#이진탐색 사용 (첫시도: 정답률 93%) 
#틀린이유: start = min(citations), end = max(ci)
#범위를 잘못잡음. 답은 0~n 사이에 존재함. 

def solution(citations):    
    answer = 0

    start = 0
    end = len(citations)
    while start <= end:    
        h = (start + end) // 2
        #h-index 찾기(h번 이상 수 h편 이상, 나머지 h 이하)
        check = 0
        for i in citations:
            if i >= h:
                check += 1
        #조건 체크
        if check >= h:
            answer = h #기록
            start = h + 1
        else: #h가 큰 경우
            end = h - 1

    return answer