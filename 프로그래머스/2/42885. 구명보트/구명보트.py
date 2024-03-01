from collections import deque 

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while len(people) > 1:
        if(people[-1] + people[0] > limit): 
            people.pop()
            answer+=1
        else:
            people.popleft()
            people.pop()
            answer+=1
        
    answer += len(people)
    return answer