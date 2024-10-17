import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0

    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        min_1 = heapq.heappop(scoville)
        min_2 = heapq.heappop(scoville)
        new_scoville = min_1 + (min_2 * 2)
        heapq.heappush(scoville, new_scoville)
        count += 1

    return count