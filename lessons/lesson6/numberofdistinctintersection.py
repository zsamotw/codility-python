def solution(N):
    pairs = 0
    circles = sorted([(point - radious, radious + point)
                      for (radious, point) in zip(N, range(0, len(N)))])
    intersections = []
    for circle in circles:
        if not intersections:
            intersections.append(circle)
        else:
            for inter in intersections:
                if inter is None:
                    pass
                elif circle[0] > inter[1]:
                    index = intersections.index(inter)
                    intersections[index] = None
                elif circle[0] >= inter[0] or circle[1] <= inter[1]:
                    pairs = pairs + 1
            intersections.append(circle)
    return pairs
