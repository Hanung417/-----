def solution(numbers, target):
    nums = len(numbers)
    count = 0
    def sim(i, answer, sign) :
        nonlocal count
        if i == nums :
            if answer == target :
                count += 1
            return
        answer = answer + numbers[i]*sign
        sim(i+1, answer, +1)
        sim(i+1, answer, -1)
            
    for sign in [1,-1] :
        sim(0, 0, sign)
    return count/2