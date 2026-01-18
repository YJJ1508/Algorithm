#순서대로 들어오고 나감: 큐 사용
#시뮬 문제
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  #[0,0] 
    truck_weights = deque(truck_weights) 
    
    curr_w = 0 #다리의 무게
    while len(truck_weights) > 0:
        #1초마다 시간 지나며 트럭 지나감
        time += 1
        curr_w -= bridge.popleft()
        
        #트럭 들어올 수 있는 경우
        if curr_w + truck_weights[0] <= weight:
            curr_w = curr_w + truck_weights[0]
            bridge.append(truck_weights.popleft()) #새 트럭 진입
        #트럭 못 들어오는 경우
        else: 
            bridge.append(0) #무게 초과 시 빈 0 추가 
            
    time += bridge_length #다리 길이 완전히 지나가기
    
    return time