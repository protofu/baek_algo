def solution(s):
    answer = ''
    # 각 문자의 첫단어만 대문자, 나머지는 모두 소문자
    words = s.split(" ")
    cap_words = [ word.capitalize() for word in words ]
    answer = ' '.join(cap_words)
    return answer