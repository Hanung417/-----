def solution(brown, yellow):
    total = brown + yellow
    for y in range(1, int(total**0.5) + 1):
        if total % y == 0:
            x = total // y
            if x >= y:
                if 2 * x + 2 * (y - 2) == brown:
                    return [x, y]