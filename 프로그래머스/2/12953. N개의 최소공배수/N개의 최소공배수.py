import math
def solution(arr):         
    answer = arr[0]
    #두개씩 lcm 뽑아서 반복 (2,6) -> 6 (6,8)-> 24 (24,14) -> 168
    for num in arr[1:]: 
        answer = answer*num // math.gcd(answer, num)

    return answer