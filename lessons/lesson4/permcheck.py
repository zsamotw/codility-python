def solution(N):
    minimum = N[0]
    maximum = 0
    length = 0
    sum_N = 0
    for el in N:
        minimum = min(minimum, el)
        maximum = max(maximum, el)
        length = length + 1
        sum_N = sum_N + el

    sum_to_minimum = ((minimum - 1) * (minimum)) // 2
    sum_to_maximum = (maximum * (maximum + 1)) // 2
    should = sum_to_maximum - sum_to_minimum

    return sum_N == should
