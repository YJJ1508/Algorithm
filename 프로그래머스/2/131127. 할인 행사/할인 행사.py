def solution(want, number, discount):
    
    num = sum(number)
    end = len(discount) - num  #number수까지 돌아주면 됨
    count = 0

    to_dict = {}
    for i in range(len(want)):
        to_dict[want[i]] = number[i] 
    
    for i in range(end+1):  #discount 순회
        temp = discount[i:i+num] 
        check = True
        for k,v in to_dict.items():
            if temp.count(k) != v:
                check = False
                break
        #할인 모두 만족
        if check == True:
            count += 1
    
    return count