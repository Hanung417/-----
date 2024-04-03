def solution(n, tops):
    dp1 = [0] * n
    dp2 = [0] * n
    dp1[0] = 1
    dp2[0] = 2 + tops[0]
    
    for i in range(1, n):
        dp1[i] = (dp1[i - 1] + dp2[i - 1]) % 10007
        dp2[i] = ((dp1[i - 1] * (1 + tops[i])) + \
                (dp2[i - 1] * (2 + tops[i]))) % 10007
        
    return (dp1[-1] + dp2[-1]) % 10007