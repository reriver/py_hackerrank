def solve(s):
    print(s)
    l = list(s)
    l[0] = l[0].capitalize()
    for i in range(1, len(l)):
        if l[i - 1].isspace():
            l[i] = l[i].capitalize()
    res = ''.join(l)
    return res


if __name__ == '__main__':
    s = input()

    result = solve(s)

    print(result)
