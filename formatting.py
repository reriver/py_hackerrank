
number = 17
wb_max = len(str(bin(number))) - 2
# print(wb, bin(number))

for i in range(1, number + 1):
    wd = len(str(i))
    # print(wd, i)
    wo = len(str(oct(i))) - 2
    # print(wo, oct(i))
    wx = len(str(hex(i))) - 2
    # print(wx, hex(i))
    wb = len(str(bin(i))) - 2
    # print(wb, bin(number))
    w1 = wb_max - wd
    w2 = wb_max - wo
    w3 = wb_max - wx
    w4 = wb_max - wb

    print("{0:s}{1:d} ".format(" " * w1, i, ""), end='')
    print("{0:s}{1:o} ".format(" " * w2, i, ""), end='')
    print("{0:s}{1:X} ".format(" " * w3, i, ""), end='')
    print("{0:s}{1:b} ".format(" " * w4, i, ""))
    # print("{0:b} ".format(i))
