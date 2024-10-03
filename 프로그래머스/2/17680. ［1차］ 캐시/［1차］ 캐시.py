def solution(cacheSize, cities):
    answer = 0
    # 캐시를 저장할 메모리 크기 [cacheSize]
    cache_memory = []
    
    for city_ori in cities:
        city = city_ori.upper()
        # cache miss 인 경우 5초 추가 및 캐시에 저장
        if city not in cache_memory:
            # cache 메모리의 사이즈가 cacheSize와 같다면
            if len(cache_memory) == cacheSize:
                # LRU(가장 오래 참조되지 않은 캐시는 제거)에 의하여 캐시 교체
                cache_memory.append(city)
                cache_memory.pop(0)
            # 크기가 넘치치 않는다면
            else:
                cache_memory.append(city)
                
            answer += 5
        # cache에 저장되어 있다면
        else:
            # LRU 알고리즘을 이용하기위해 가장 뒤로 보내기
            cache_memory.remove(city)
            cache_memory.append(city)
            answer += 1
    
    return answer