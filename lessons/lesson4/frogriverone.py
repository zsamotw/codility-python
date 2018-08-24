def solution(N, n):
    time = -1
    for i in range(0, len(N)):
        if N[i] == (n):
            time = i
    return time
