import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    current_time = 0
    total_time = 0
    min_heap = []
    i = 0
    
    while i < n or min_heap:
        while i < n and jobs[i][0] <= current_time:
            heapq.heappush(min_heap, (jobs[i][1], jobs[i][0]))
            i += 1
        
        if min_heap:
            process_time, start_time = heapq.heappop(min_heap)
            current_time += process_time
            total_time += current_time - start_time
        else:
            current_time = jobs[i][0]
    

    return total_time // n