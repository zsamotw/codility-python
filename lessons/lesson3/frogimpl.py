def solution(X, Y, D):
    distance = Y - X
    return distance // D if distance % D == 0 else distance // D + 1
