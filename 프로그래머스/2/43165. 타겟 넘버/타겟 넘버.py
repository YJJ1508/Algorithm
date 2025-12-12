#이진 트리 형식이면 bfs,dfs 염두에 두기
def solution(numbers, target):
    count = 0
    bfs = [0]

    for i in numbers:
        temp = []
        #각각의 numbers +i/-i 반복
        for j in bfs:
            temp.append(j+i)
            temp.append(j-i)
        bfs = temp
    
    for a in bfs:
        if a == target:
            count += 1

    return count