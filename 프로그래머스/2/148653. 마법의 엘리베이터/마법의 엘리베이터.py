def solution(storey):
    answer = 0

    while storey:
        stage = storey % 10
        if stage > 5:
            answer += (10 - stage)
            storey += 10
        elif stage < 5:
            answer += stage
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += stage
        storey //= 10

    return answer