def valid(fn):
    return lambda sides: all(sides) and 2 * max(sides) < sum(sides) and fn(
        sides)


@valid
def equilateral(sides):
    return sides[0] != 0 and len(set(sides)) == 1


@valid
def isosceles(sides):
    return len(set(sides)) < 3


@valid
def scalene(sides):
    return len(set(sides)) == 3
