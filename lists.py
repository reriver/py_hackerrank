def do_insert(s, ints):
    ints.insert(int(s[1]), int(s[2]))


def do_print(s, ints):
    print(ints)


def do_remove(s, ints):
    if ints.count(int(s[1])) > 0:
        ints.remove(int(s[1]))
    else:
        print("no", int(s[1]), "at the list")


def do_append(s, ints):
    ints.append(int(s[1]))


def do_sort(s, ints):
    ints.sort()


def do_pop(s, ints):
    ints.pop()


def do_reverse(s, ints):
    ints.reverse()


if __name__ == '__main__':
    N = int(input())

    ints_list = []

    for i in range(N):
        s = input().split()

        options = {
            'insert': do_insert,
            'print': do_print,
            'remove': do_remove,
            'append': do_append,
            'sort': do_sort,
            'pop': do_pop,
            'reverse': do_reverse,
        }

        options[s[0]](s, ints_list)
