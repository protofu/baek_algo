def solution(sizes):
    big = []
    small = []
    # 각 쌍 중 큰거 한쪽으로 작은거 한쪽으로 몰아넣고
    for col, row in sizes:
        if col>row:
            big.append(col)
            small.append(row)
        else:
            big.append(row)
            small.append(col)   
    # 각 리스트에서 max값 추출해서 곱하기
    return max(big) * max(small)