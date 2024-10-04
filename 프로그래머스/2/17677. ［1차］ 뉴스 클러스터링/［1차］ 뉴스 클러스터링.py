def solution(str1, str2):
    # 두 문자열 모두 대문자화
    str1 = str1.upper()
    str2 = str2.upper()
    
    # 2알파벳씩 끊어서 리스트화, 알파벳 쌍만 포함
    a = []
    for i in range(len(str1) - 1):
        pair = str1[i:i + 2]
        if pair.isalpha():  # 두 글자가 모두 알파벳인지 체크
            a.append(pair)
    
    b = []
    for i in range(len(str2) - 1):
        pair = str2[i:i + 2]
        if pair.isalpha():  # 두 글자가 모두 알파벳인지 체크
            b.append(pair)
    
    # 다중집합을 위해 각 리스트의 요소 수 세기
    a_count = {}
    b_count = {}
    
    for item in a:
        if item in a_count:
            a_count[item] += 1
        else:
            a_count[item] = 1

    for item in b:
        if item in b_count:
            b_count[item] += 1
        else:
            b_count[item] = 1

    # 교집합과 합집합 계산
    intersection_count = 0
    union_count = 0
    
    # 교집합 계산
    for item in a_count:
        if item in b_count:
            intersection_count += min(a_count[item], b_count[item])
    
    # 합집합 계산
    union_count = sum(a_count.values()) + sum(b_count.values()) - intersection_count
    
    # 자카드 유사도 계산
    if union_count == 0:  # 두 집합이 모두 공집합인 경우
        jaccard_similarity = 1
    else:
        jaccard_similarity = intersection_count / union_count

    # 65536에 곱하고 소수점 버리기
    answer = int(jaccard_similarity * 65536)
    return answer