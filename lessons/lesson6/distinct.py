def solution(N):
    if N == []:
        return 0
    sorted_N = sorted(N)
    head, *tail = sorted_N
    distinct = 1
    for el in tail:
        if el != head:
            distinct = distinct + 1
            head = el
    return distinct
