def solution(progresses, speeds):
    answer = []
    days_to_complete = []

    for progress, speed in zip(progresses, speeds):
        remaining_progress = 100 - progress
        if remaining_progress % speed == 0:
            days = remaining_progress // speed
        else:
            days = remaining_progress // speed + 1
        days_to_complete.append(days)

    current_max_day = days_to_complete[0]
    count = 0

    for day in days_to_complete:
        if day > current_max_day:
            answer.append(count)
            count = 1
            current_max_day = day
        else:
            count += 1
            
    answer.append(count)

    return answer