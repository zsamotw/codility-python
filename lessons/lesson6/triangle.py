def solution(N):
    assert(len(N) >= 3)
    N_sorted = sorted(N)
    for i in range(0, len(N_sorted) - 1):
        for j in range(i + 2, len(N_sorted) - 1):
            if N_sorted[i] + N_sorted[i + 1] >= N_sorted[j]:
                return True
    return False
