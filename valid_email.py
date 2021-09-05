import string


def fun(s):
    try:
        name, site = s.split('@')
    except ValueError:
        return False
    try:
        www, ext = site.split('.')
    except ValueError:
        return False

    validzonechars = string.ascii_letters
    if not all([c in validzonechars for c in ext]) or len(ext) > 3:
        return False
    validsitechars = validzonechars + string.digits
    if not all([c in validsitechars for c in www]) or len(www) < 1:
        return False
    validnamechars = validsitechars + '-' + '_'
    if not all([c in validnamechars for c in name]) or len(name) < 1:
        return False
    return True

if __name__ == '__main__':
    n = int(input())

    mails = []
    for _ in range(n):
        s = input()
        if fun(s):
            mails.append(s)

    print(mails)
    