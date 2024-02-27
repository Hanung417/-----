def hanoi(n, start, sub, end, answer = []):
    if n == 1 :
        answer += [[start, end]]
        return 
    else :
        hanoi(n-1, start, end, sub)
        answer += [[start, end]]
        hanoi(n-1, sub, start, end)
    return answer

def solution(n):      
    return hanoi(n,1,2,3)