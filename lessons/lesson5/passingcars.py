#0 east -->
#1 west <--


def solution(A):
    east_cars = 0
    passing = 0
    for car in A:
        if car == 1:
            passing = passing + east_cars
        elif car == 0:
            east_cars = east_cars + 1

    return passing
