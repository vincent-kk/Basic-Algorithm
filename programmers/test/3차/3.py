from collections import deque


def solution(cacheSize, cities):
    if cacheSize < 1:
        return len(cities) * 5

    cache = deque()
    time = 0
    for city in cities:
        city = city.upper()
        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
            time += 1

        else:
            if len(cache) >= cacheSize:
                cache.pop()
            cache.appendleft(city)
            time += 5

    return time