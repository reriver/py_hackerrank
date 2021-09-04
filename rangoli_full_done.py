import string

n = int(input())

abc = '-' + '-'.join(list(string.ascii_lowercase[1:n])) + '-' * (n - 1) * 2
cba = '-' * (n - 1) * 2 + '-'.join(reversed(list(string.ascii_lowercase[:n])))
print('abc', abc)
print('cba', cba)
size = 2 * (n * 2 - 1) - 1 #2*N - 2 -1 + n*2
print('size', size)
cbabc = cba + abc
print(cbabc, '\n')

end_offset = len(cba)
print('end_offset', end_offset)
for i in range(n):
    print(i, cbabc[i * 2:n * 2 + i * 2] + abc[n * 2 - 1 - i * 2:n * 2 - 1 - i * 2 + n * 2 - 3])
for i in range(n - 2, -1, -1):
    print(i, cbabc[i * 2:n * 2 + i * 2] + abc[n * 2 - 1 - i * 2:n * 2 - 1 - i * 2 + n * 2 - 3])

#
# j = 1
# dash_num = 2 * (n - 1 - j)
# abc_num2 = abc[2 * n - 2 - 2 * j:2 * n - 1]
# cba_num2 = cba[26*2 - 2 - int(size/2):26*2 - 2 - int(size/2) + j * 2]
# cbabc_n2 = cba_num2 + abc_num2
# print('\nabc_num2', abc_num2)
# print('cba_num2', cba_num2)
# print('cbabc', cbabc_n2)
# abc2 = '-'.join(list(string.ascii_lowercase)[:j]) + '-'.join(reversed(list(string.ascii_lowercase)))
# print(abc2)
# row2 = '-' * dash_num + str(abc2[2 * (n - 1 - j):2 * (n - 1) + 1]) + '-' * dash_num
# print(row2)
