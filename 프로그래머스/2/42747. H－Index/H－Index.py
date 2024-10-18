def solution(citations):
    n = len(citations)
    citations.sort(reverse = True)
    for i, cit in enumerate(citations):
        if i + 1 > cit:
            return i
    
    return len(citations)
