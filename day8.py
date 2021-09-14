#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    book = dict()

    for _ in range(n):
        name, cell = input().split()
        book[name] = cell

    while True:
        try:
            line = input()
            if line in book.keys():
                print("{0}={1}".format(line, book[line]))
            else:
                print("Not found")
        except EOFError:
            break
