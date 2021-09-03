if __name__ == '__main__':
    n = int(input())

    students = []
    marks = set()
    for i in range(n):
        name = input()
        mark = float(input())
        marks.add(mark)
        st = [mark, name]
        students.append(st)
    # marks
    m = list(marks)
    m.sort()
    print(m)
    second_lowest_mark = m[1]

    output = []
    for key, value in students:
        if key == second_lowest_mark:
            output.append(value)

    print(m)
    print(students)
    output.sort()
    print('\n'.join(output))
