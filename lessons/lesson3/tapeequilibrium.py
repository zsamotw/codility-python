def solution(N):

    sum = 0
    length = 0

    for el in N:
        sum = sum + el
        length = length + 1

    first = N[0]
    rest = sum - first
    min = rest - first

    for i in range(1, length - 1):
        loop_first = first + N[i]
        loop_rest = rest - N[i]
        loop_diff = abs(loop_rest - loop_first)
        if min > loop_diff:
            min = loop_diff
        first = loop_first
        rest = loop_rest

    return min
