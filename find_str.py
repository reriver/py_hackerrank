def count_substring(s, sub):
    occurs_count = 0
    for i in range(len(s)):
        f = s[i:len(s)].find(sub)
        if f == 0:
            occurs_count += 1
            print(occurs_count, s[i:len(s)])
    return occurs_count

if __name__ == '__main__':
    s = input()
    sub = input()
    res = count_substring(s, sub)
    print(res)