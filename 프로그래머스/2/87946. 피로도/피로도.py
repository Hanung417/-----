def solution(k, dungeons):
    max_explored = 0
    n = len(dungeons)
    visited = [False] * n
    
    def dfs(current_stamina, count):
        nonlocal max_explored
        max_explored = max(max_explored, count)
        for i in range(n):
            if not visited[i] and current_stamina >= dungeons[i][0]:
                visited[i] = True
                dfs(current_stamina - dungeons[i][1], count + 1)
                visited[i] = False

    dfs(k, 0)
    return max_explored