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


### yield를 이용하여 메모리의 사용량을 줄임 ###
def solution(n):

    def hanoi(n, start, sub, end):
        if n == 1:
            yield [start, end]
        else:
            yield from hanoi(n-1, start, end, sub)
            yield [start, end]
            yield from hanoi(n-1, sub, start, end)

    answer = list(hanoi(n, 1, 2, 3))
    return answer
