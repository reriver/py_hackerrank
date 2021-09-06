n, m = input().split()
print(n, m)
ints_str = input().split()
ints_list = [int(x) for x in ints_str]
print(ints_list)
a_str = input().split()
A = set([int(x) for x in a_str])
print(A)
b_str = input().split()
B = set([int(x) for x in b_str])
print(B)
happy = 0
for i in ints_list:
    if i in A:
        happy += 1
    if i in B:
        happy -= 1
print(happy)
