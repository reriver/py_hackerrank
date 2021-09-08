def jumpingOnClouds(c):
    steps = 0
    i = 0
    l = len(c)
    print(c)
    while i != l - 1:
        if i + 2 < l and c[i + 2] != 1:
            i += 2
            steps += 1
        elif i + 1 < l and c[i + 1] != 1:
            i += 1
            steps += 1
        else:
            return 0
    return steps


if __name__ == '__main__':
    s = input().split()
    c = [int(i) for i in s]
    print(c)
    print(jumpingOnClouds(c))
