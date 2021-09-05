if __name__ == '__main__':
    th = int(input())
    c = 'H'

    # Top Cone
    for i in range(th):
        print((c * i).rjust(th - 1) + c + (c * i).ljust(th - 1))

    # Top Pillars
    for i in range(th + 1):
        print((c * th).center(th * 2) + (c * th).center(th * 6))

    # Middle Belt
    for i in range((th + 1) // 2):
        print((c * th * 5).center(th * 6))

        # Bottom Pillars
    for i in range(th + 1):
        print((c * th).center(th * 2) + (c * th).center(th * 6))

        # Bottom Cone
    for i in range(th):
        print(((c * (th - i - 1)).rjust(th) + c + (c * (th - i - 1)).ljust(th)).rjust(th * 6))