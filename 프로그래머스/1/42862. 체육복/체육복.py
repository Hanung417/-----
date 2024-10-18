def solution(n, lost, reserve):
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    attend_count = n - len(lost_set)
    for lost_student in sorted(lost_set):
        if lost_student - 1 in reserve_set:
            reserve_set.remove(lost_student - 1)
            attend_count += 1
        elif lost_student + 1 in reserve_set:
            reserve_set.remove(lost_student + 1)
            attend_count += 1
    
    return attend_count