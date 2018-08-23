def solution(N, n):
    time = -1
    for i in range(0, len(N)):
        print('{} {}'.format(i, N[i]))
        if N[i] == (n):
            time = i
    return time
