import math

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.scores = scores
        for s in self.scores:
            if s < 0 or 100 < s:
                print("Error")
                return
        super(Student, self).__init__(firstName, lastName, idNumber)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        grades = "TDPAEO"
        average = sum(self.scores) / len(self.scores)
        print(average)
        print(int(average))
        if 90 <= average:
            return grades[5]
        elif int(average) in range(80, 90):
            return grades[4]
        elif int(average) in range(70, 80):
            return grades[3]
        elif int(average) in range(55, 70):
            return grades[2]
        elif int(average) in range(40, 55):
            return grades[1]
        elif int(average) in range(0, 40):
            return grades[0]

if __name__ == '__main__':
    line = input().split()
    print(line)
    n = int(input())
    sc = [0] * n
    in1 = input().split()
    for i in range(n):
        sc[i] = int(in1[i])
    stud = Student(line[0], line[1], int(line[2]), sc)
    print(stud.calculate())
