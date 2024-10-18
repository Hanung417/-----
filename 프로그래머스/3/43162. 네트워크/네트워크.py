def solution(n, computers):
    def dfs(computer, visited):
        stack = [computer]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for connected, is_connected in enumerate(computers[node]):
                    if is_connected and not visited[connected]:
                        stack.append(connected)
    
    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            dfs(i, visited)
            network_count += 1
    
    return network_count
