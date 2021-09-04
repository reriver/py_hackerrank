import string

n = int(input())

if n == 1:
    print('a')
    exit()


abc = '-' + '-'.join(list(string.ascii_lowercase[1:n])) + '-' * (n - 1) * 2
cba = '-' * (n - 1) * 2 + '-'.join(reversed(list(string.ascii_lowercase[:n]))) + '-'

for i in range(n):
    end_offset = n * 2 - 1 - i * 2
    print(cba[i * 2:i * 2 + n * 2] + abc[end_offset:end_offset + n * 2 - 3])
for i in range(n - 2, -1, -1):
    end_offset = n * 2 - 1 - i * 2
    print(cba[i * 2:i * 2 + n * 2] + abc[end_offset:end_offset + n * 2 - 3])
