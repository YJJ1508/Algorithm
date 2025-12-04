from collections import deque
def solution(progresses, speeds):
    answer = [] 
    
    #배포되는 날짜 계산
    date = deque() #[7,3,9]
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
        date.append(day)
    
    #각 배포마다 몇개 배포되는지 확인
    while date: #[7,3,9]
        d = date.popleft()  #7
        count = 1
        #함께 배포될수 있는지 카운트
        temp = date
        while date and d >= date[0]: #3 9
            count += 1
            date.popleft()
        answer.append(count)

    return answer