def solution(A, K):
    result = A
    for i in range(0, K):
        *infix, post = result
        result = [post] + result[:-1]
    return result
