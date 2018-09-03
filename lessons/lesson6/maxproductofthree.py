def solution(N):
    assert (len(N) >= 3)

    sorted_N = sorted(N)
    *init, a, b, c = sorted_N
    return a * b * c
