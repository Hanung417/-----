def solution(n):
    step= [0 for i in range(n+1)]
    step[:2] = [1,1]
    for i in range(2, n+1):
        step[i] = step[i-1] + step[i-2]
    return step[-1] % 1234567
 
 ### 재귀 이용 ###
def solution(n):
    def JumpCase(num):
        return (JumpCase(num-1) + JumpCase(num-2)) if num > 2 else num
    answer = JumpCase(n)
    return answer

### math 라이브러리의 팩토리얼 사용 ###
import math
def jumpCase(n):
    num = n//2
    answer = 0
    for i in range(num+1):
        a = num-i
        answer += math.factorial(a)//(math.factorial(i)*math.factorial(a-i))
    return answer
