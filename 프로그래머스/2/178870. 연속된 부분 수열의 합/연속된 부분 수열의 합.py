from collections import deque
def solution(sequence, k):
    result = [0,0]
    min_len = 10**9
    
    q = deque()
    sum_s = 0
    #합이 k인 부분수열 담기
    for i in range(len(sequence)):
        q.append(i) 
        sum_s += sequence[i]
        
        #합이 k보다 크면 왼쪽에서 빼기
        while q and sum_s > k:
            idx = q.popleft()
            sum_s -= sequence[idx]
        #합이 k일때
        if sum_s == k:
            current_len = len(q)
            # 지금 찾은 수열이 이전에 찾은 것보다 짧다면 정답 갱신
            if current_len < min_len:
                min_len = current_len
                result = [q[0], q[-1]]
    
    return result