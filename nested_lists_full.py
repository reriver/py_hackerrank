if __name__ == '__main__':
    n = int(input())

    students = []
    marks = []
    for i in range(n):
        name = input()
        mark = float(input())
        marks.append(mark)
        st = [mark, name]
        # marks[mark] = name
        # students.append([input(), input()])
        # students[mark] = name
        students.append(st)

    print(marks)
    marks.sort()
    print(marks)
    print(marks[1])
    second_lowest_mark = marks[1]
    print(students)
    output = []
    # for v in students:
    #     if marks[1] == v[0]:
    #         print(v[1])
    for key, value in students:
        if key == second_lowest_mark:
            print(value)
            output.append(value)

    output.sort()
    print(output)
    print('\n'.join(output))
    #
    # marks = []
    # for i in range(n):
    #     marks.append([input(), input()])
    #
    # print(marks)