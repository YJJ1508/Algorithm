#틀린이유: 첨엔 구현으로 접근했었음..
def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True) #문자열로 크기 비교
    
    for i in numbers:
        answer += i
    
    return str(int(answer)) #예외케이스: '000'일 경우 0으로 출력 위함