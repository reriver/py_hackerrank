if __name__ == '__main__':
    n1 = int(input())
    s1 = set(input().split(' '))
    n2 = int(input())
    s2 = set(input().split(' '))
    print(s1, s2)
    d = s1.symmetric_difference(s2)
    print(d)
    li = list(d)
    print(li)
    ints = [int(x) for x in li]
    print('unsorted', ints, type(ints))
    ints.sort(reverse=False)
    print('sorted', ints, type(ints))

    for i in ints:
        print(i)

