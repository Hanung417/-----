def location(n, q, r) :
    answer = 0
    if n == r :
        return 1
    for c in range(n) :
        q[r] = c
        for i in range(r) :
            if q[i] == q[r] or abs(q[i]-q[r]) == (r-i) :
                break
        else :
            answer += location(n, q, r+1)
    return answer

def solution(n):
    q = [0]*n
    return location(n, q, 0)