def solution(n, A):
    counters = [0] * n
    maximum = 0
    for index in A:
        if index <= n:
            counters[index - 1] = counters[index - 1] + 1
            maximum = max(maximum, counters[index - 1])
        else:
            counters = [maximum] * n
    return counters
