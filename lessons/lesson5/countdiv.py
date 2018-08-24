def solution(A, B, K):
    result = B//K - A // K
    return result + 1 if A % K == 0 else result
