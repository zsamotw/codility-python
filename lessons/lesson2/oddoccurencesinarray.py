def solution(N):
    checked = [] 
    for el in N:
        if el in checked:
            checked.remove(el)
        else:
            checked.append(el)
    return checked[0]
