def solution(N):
    sum = 0
    length = 0
    for el in N:
        sum = sum + el
        length = length + 1
    return ((length + 1) * (length + 2)) // 2 - sum
