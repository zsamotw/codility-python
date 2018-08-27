def solution(N):
    def prefix_sum(N):
        n = len(N)
        P = [0] * (n + 1)
        for k in range(1, n + 1):
            P[k] = P[k - 1] + N[k - 1]
        return P
    min_avg = (None, None)   # (avg, index)
    P = prefix_sum(N)
    for i in range(2, len(P)):
        for j in range(0, i - 1):
            avg = (P[i] - P[j]) / (i - j + 1)
            if (min_avg[0] is None) or (min_avg[0] > avg):
                min_avg = (avg, j)

    return min_avg[1]
