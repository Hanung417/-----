def solution(n):
    step= [0 for i in range(n+1)]
    step[:2] = [1,1]
    for i in range(2, n+1):
        step[i] = step[i-1] + step[i-2]
    return step[-1] % 1234567