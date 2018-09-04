def solutions(N):
    pairs = 0
    circles = sorted([(point - radious, radious + point)
                      for (radious, point) in zip(N, range(0, len(N)))])
    print(circles)
    in_use = []
    for circle in circles:
        for used in in_use:
            print(in_use)
            if circle[0] > used[1]:
                in_use.remove(circle)
            if circle[0] >= used[0] and circle[1] <= used[1]:
                pairs = pairs + 1
            in_use.append(circle)
    return pairs


print(solutions([10, 11, 12]))
