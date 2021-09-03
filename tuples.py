import hashlib

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    # n = int(input())
    # l = [int(x) for x in input().split()]
    # t = tuple(integer_list[:n])
    t = tuple(integer_list)

    h = hash(t)
    print(h)
