steps = int(input())
path = list(input())
print(path)

h = 0
valley = 0
for i in path:
    if i == 'U':
        if h + 1 == 0:
            valley += 1
        h += 1
    if i == 'D':
        h -= 1
# return(valley)
print(valley)
