import heapq
def dijkstra(d, graph):
    heap = []
    heapq.heappush(heap, [0,1]) #시작노드(거리,노드)
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in graph[node]:
            if cost + c < d[n]:
                d[n] = cost + c
                heapq.heappush(heap, [cost+c,n])

def solution(N, road, K):
    d = [10**6] * (N+1)
    d[1] = 0
    
    #다익스트라 실행
    graph = [[] for _ in range(N+1)]
    for x,y,z in road:
        graph[x].append([z,y])  #거리,노드
        graph[y].append([z,x]) 
    dijkstra(d, graph)
    
    #K이하 노드 수 리턴
    result = 0
    for i in d:
        if i <= K:
            result += 1
            
    return result