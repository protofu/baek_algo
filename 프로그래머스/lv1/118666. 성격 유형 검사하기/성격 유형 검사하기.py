def solution(survey, choices):
    mbti = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(choices)):
        if choices[i] < 4:
            mbti[survey[i][0]] += (choices[i] * 3) % 4
        if choices[i] > 4:
            mbti[survey[i][1]] += choices[i] % 4
    mbti_key = list(mbti.keys())
    
    answer = ''
    for i in range(0, len(mbti_key), 2):
        if mbti[mbti_key[i]] > mbti[mbti_key[i+1]]:
            answer += mbti_key[i]
        elif mbti[mbti_key[i]] < mbti[mbti_key[i+1]]:
            answer += mbti_key[i+1]
        else:
            answer += min(mbti_key[i], mbti_key[i+1])
    return answer