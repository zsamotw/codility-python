def to_binary(N, res=[]):
    if N == 1:
        return res + [1]
    else:
        return to_binary((N // 2), res + [N % 2])


def solution(N):

    result = 0
    inLoop = 0
    is_one_before = False
    Bn = to_binary(N)

    for el in Bn:
        if el == 0:
            if is_one_before:
                inLoop = inLoop + 1
        else:                            # el is 1
            if is_one_before:
                if inLoop > result:
                    result = inLoop
                    inLoop = 0
                else:
                    inLoop = 0
            elif not is_one_before:
                is_one_before = True

    return result
