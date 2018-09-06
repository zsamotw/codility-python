def solution(A, B):
    fishes = [(size, direction) for (size, direction) in zip(A, B)]
    fish_stack = []
    for fish in fishes:
        if not fish_stack:
            fish_stack.append(fish)
        else:
            stack = fish_stack[:]
            for f in fish_stack:
                if f[1] == 1 and fish[1] == 0 and f[0] < fish[0]:
                    # loop(stack, fish)
                    stack.remove(f)

                elif f[1] == 1 and fish[1] == 0 and f[0] > fish[0]:
                    break
                else:
                    stack = [fish] + stack
                    break
            fish_stack = stack
            if not fish_stack:
                fish_stack.append(fish)
    return len(fish_stack)
