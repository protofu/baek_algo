def solution(s):
    answer = ''
    # 공백 단위로 나눠서 list화
    w_numbers = s.split(' ')
    numbers = [int(number) for number in w_numbers]
    answer = str(min(numbers)) + ' ' + str(max(numbers))
    return answer