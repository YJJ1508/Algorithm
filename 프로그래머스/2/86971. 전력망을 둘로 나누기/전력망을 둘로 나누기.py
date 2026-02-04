def dfs(graph,visited,start):
    visited[start] = True
    count = 1 
    
    for i in graph[start]:
        if visited[i] == False:
            count += dfs(graph,visited,i)
            
    return count
    

def solution(n, wires):    
    #그래프 초기화
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    #모든 노드 하나씩 끊어주기
    result = n    
    for a, b in wires:
        visited = [False] * (n+1)
        #간선지우기(방문으로 처리)
        visited[b] = True
        #a가 속한 노드 개수 
        cnt = dfs(graph, visited, a)
        
        #차이 계산
        diff = abs(cnt - (n-cnt))
        result = min(result, diff) 
        
    return result