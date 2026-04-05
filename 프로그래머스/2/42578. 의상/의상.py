def solution(clothes):
    c = {}
    #1.종류별로 분류  
    for name, kind in clothes:
        if kind not in c:
            c[kind] = [name]
        else:
            c[kind] += [name]
     
    count = 1
    #2.조합 개수 세기 (a+1)(b+1) -> ab,a,b,1 
    for k,v in c.items():  
        count *= (len(v)+1)    
        
    return count -1 #모든거 입지않은 1 케이스 빼주기
        
     
