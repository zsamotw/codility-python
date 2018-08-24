def solution(S, P, Q): #O(n + m)

    def add(t, ch):
        if ch == 'A':
            return (t[0] + 1, t[1], t[2], t[3])
        elif ch == 'C':
            return (t[0], t[1] + 1, t[2], t[3])
        elif ch == 'G':
            return (t[0], t[1], t[2] + 1, t[3])
        elif ch == 'T':
            return (t[0], t[1], t[2], t[3] + 1)
    # end add

    def prefix_sum(S):
        n = len(S)
        P = [(0,0,0,0)] * (n + 1)

        for k in range(1, n + 1):
            P[k] = add(P[k - 1],  S[k - 1])
        return P
        # end prefix_sum

    def count_total(P, x, y):
        return (P[y + 1][0] - P[x][0], P[y + 1][1] - P[x][1], P[y + 1][2] - P[x][2], P[y + 1][3] - P[x][3])
    # end count_total

    def min_factor(t):
        factor = 0
        for value in t:
            factor = factor + 1
            if value > 0:
                return factor
    # end min_factor

    prefix_sum_P = prefix_sum(S)
    result = []
    for t in list(zip(P, Q)):
        tuple_in_loop = count_total(prefix_sum_P, t[0], t[1])
        min = min_factor(tuple_in_loop)
        result.append(min)
    return result


res = solution("ACG", [0,1], [2,1])


# res = solution("AAAC", [0], [2])


def solutionN2(S,P,Q): # o(n2)
    def parse(seq):
        parsed = []
        for ch in seq:
            if ch == 'A': parsed.append(1)
            elif ch == 'C': parsed.append(2)
            elif ch == 'G': parsed.append(3)
            elif ch == 'T': parsed.append(4)
        return parsed
    # end parse

    result = []
    for t in list(zip(P, Q)):
        seq = S[t[0]:t[1] + 1]
        minimum = min(parse(seq))
        result.append(minimum)

    return result
