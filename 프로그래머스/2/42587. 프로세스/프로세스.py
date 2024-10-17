from collections import deque

def solution(priorities, location):
    queue = deque((priority, i) for i, priority in enumerate(priorities))
    cnt = 0
    
    while queue:
        current = queue.popleft()
        if any(current[0] < other[0] for other in queue):
            queue.append(current)
        else:
            cnt += 1
            if current[1] == location:
                return cnt