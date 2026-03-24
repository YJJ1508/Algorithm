#처음과 마찬가지로 또 dp로 접근해서 틀림(시간초과는 예상하고 루프를 반만큼 돌리는식으로 품..)
#버트-> 간단히 수학적으로 접근하면 끝(그리디)
def solution(n):
    amount = 0
    while n != 0:
        #순간이동
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            amount += 1
    
    return amount
    
    


