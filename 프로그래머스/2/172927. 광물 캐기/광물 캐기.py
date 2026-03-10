def solution(picks, minerals):
    total_picks = 0
    for x in picks:
        total_picks += x
    
    #캘 수 있는 광물의 개수
    if len(minerals) > total_picks * 5:
        minerals = minerals[:total_picks*5]
    
    #5개씩 광물 개수 카운트
    cnt_m = [[0,0,0] for x in range(10)]  #dia,철,돌
    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            cnt_m[i//5][0] += 1
        elif minerals[i] == "iron":
            cnt_m[i//5][1] += 1
        else:
            cnt_m[i//5][2] += 1
    
    #피로도가 높은 순서대로 광물 정렬   #[[3,2,0],[1,1,1]]
    cnt_m = sorted(cnt_m, key=lambda x: (-x[0],-x[1],-x[2]))
    
    #피로도 계산
    answer = 0 
    for mineral in cnt_m:   
        d,i,s = mineral
        for idx in range(3):  #picks 선택
            #dia 곡괭이 1순위
            if idx==0 and picks[idx] > 0:
                answer += d+i+s
                picks[idx] -= 1
                break 
            #iron 곡괭이 2순위
            if idx==1 and picks[idx] > 0:
                answer += d*5 + i + s
                picks[idx] -=1
                break
            #stone 곡괭이 3순위
            if idx==2 and picks[idx] > 0:
                answer += d*25 + i*5 + s
                picks[idx] -= 1
                break     
    
    return answer