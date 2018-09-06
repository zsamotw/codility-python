def solution(N):
    pairs = 0
    circles = sorted([(point - radious, radious + point)
                      for (radious, point) in zip(N, range(0, len(N)))])
    print(circles)
    intersections = []
    for circle in circles:
        print('intersections {}'.format(intersections))
        print('circle: {}'.format(circle))
        if not intersections:
            intersections.append(circle)
        else:
            for inter in intersections:
                print('inter: {}'.format(inter))
                if inter is None:
                    pass
                elif circle[0] > inter[1]:
                    print('inter to remove')
                    index = intersections.index(inter)
                    intersections[index] = None
                # elif circle[1] <= inter[1]:
                elif circle[0] >= inter[0] or circle[1] <= inter[1]:
                    print('pair ++')
                    pairs = pairs + 1
            print('add circle to intersections')
            intersections.append(circle)
    return pairs


print(solution([1, 5, 2, 1, 4, 0]))
