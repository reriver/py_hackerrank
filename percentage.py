if __name__ == '__main__':
    n = int(input())

    students = {}
    for i in range(n):
        in1 = input().split()
        st_name = in1[0]
        marks = [float(in1[1]), float(in1[2]), float(in1[3])]
        students[st_name] = sum(marks)/len(marks)
    name = input()

    print("{0:.2f}".format(students[name]))


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()