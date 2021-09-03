if __name__ == '__main__':
    n = int(input())

    students = []
    marks = []
    for i in range(n):
        name = input()
        mark = float(input())
        marks.append(mark)
        st = [mark, name]
        students.append(st)
    marks.sort()
    second_lowest_mark = marks[1]

    output = []
    for key, value in students:
        if key == second_lowest_mark:
            output.append(value)

    output.sort()
    print('\n'.join(output))
