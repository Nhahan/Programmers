def solution(sizes):
    max_l = 0
    max_r = 0
    for size in sizes:
        if size[1] > size[0]:
            size[0], size[1] = size[1], size[0]
        if size[0] > max_l:
            max_l = size[0]
        if size[1] > max_r:
            max_r = size[1]
    return max_l * max_r
