# def solution(k, dungeons):
#     answer = 0
#     dungeons.sort(key=lambda x:x[1])
#     for dun in dungeons:
#         if dun[0] <= k:
#             k -= dun[1]
#             answer += 1
#         else:
#             break
#     return answer


from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for random in permutations(dungeons, len(dungeons)):
        cnt = 0
        tired = k
        for dun in random:
            if tired >= dun[0]:
                tired -= dun[1]
                cnt += 1
            else:
                break
        if cnt > answer:
            answer = cnt

    return answer