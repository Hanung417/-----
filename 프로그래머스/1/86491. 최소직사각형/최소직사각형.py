def solution(sizes):
    answer = 0
    sorted_sizes = [sorted(size) for size in sizes]
    width = max(size[0] for size in sorted_sizes)
    height = max(size[1] for size in sorted_sizes)
    answer = width *height
    return answer