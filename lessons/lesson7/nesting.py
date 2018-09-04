def solution(N):
    opens = 0
    for ch in N:
        if ch == '(':
            opens = opens + 1
        elif ch == ')' and opens > 0:
            opens = opens - 1
        elif ch == ')' and opens <= 0:
            return 0
    if opens == 0:
        return 1
    else:
        return 0
