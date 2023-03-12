from itertools import permutations

def is_prime_number(num) :
    if num < 2 :
        return False
    
    for j in range(2, num) :
        if num % j == 0 :
            return False
            
    return True

def solution(numbers):
    answer = 0
    num_lst = []
    for i in range(1, len(numbers)+1):
        num_lst.append(list(set(map(''.join, permutations(numbers, i)))))
    num_lst = list(set(map(int, set(sum(num_lst, [])))))
    
    for i in num_lst:
        if is_prime_number(i):
            answer += 1
    return answer