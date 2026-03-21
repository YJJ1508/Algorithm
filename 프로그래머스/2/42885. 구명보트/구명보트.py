def solution(people, limit):
    count = 0
    l, r = 0, len(people)-1
    people.sort()
    
    while l <= r:
        if people[l] + people[r] <= limit:    #동반 가능한 경우
            l += 1
            r -= 1
            count += 1
        else:   #동반할 수 없음(혼자 이동)
            r -= 1
            count += 1

    return count
        