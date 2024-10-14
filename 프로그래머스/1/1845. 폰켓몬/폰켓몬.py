def solution(nums):
    answer = 0
    N = len(nums) // 2
    A = len(set(nums))
    
    answer = min(N,A)
    return answer