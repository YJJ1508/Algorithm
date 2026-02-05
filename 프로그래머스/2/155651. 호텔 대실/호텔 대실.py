import heapq
def solution(book_time):    
    #시간 분으로 환산
    b = []
    for s,e in book_time:
        h1,m1 = map(int, s.split(":"))
        h2,m2 = map(int, e.split(":"))
        b.append([h1*60+m1, h2*60+m2+10])
    b.sort() 
        
    #방 배정
    rooms = []
    for start, end in b:
        #가장 빨리 비는 방과 비교
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)   
            
        #새방 배정
        heapq.heappush(rooms, end) 
            

    return len(rooms)