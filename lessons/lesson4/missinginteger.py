def solution(N):
    contener = [None] * 100000
    minimum = N[0] if N[0] >= 0 else 1
    for el in N:
        if el >= 0:
            contener[el] = 1
            minimum = min(minimum, el) if el > 0 else minimum

    for index in range(minimum, 100000):
        if(contener[index]) is None:
            return index
    return 1

res = solution([1, -3,3,4,-3,10])
res = solution([-3, -2])
res = solution([7,-1, 0,-3, -2])
