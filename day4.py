class Person:
    print_new_line = False

    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge >= 0:
            self.age = initialAge
        else:
            self.age = 0
            print("Age is not valid, setting age to 0. ", end="")
            Person.print_new_line = True

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if Person.print_new_line:
            print("")
        Person.print_new_line = True
        if self.age in range(13):
            print("You are young.", end='')
        elif self.age in range(13, 18):
            print("You are a teenager.", end='')
        else:
            print("You are old.", end='')

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1

if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        age = int(input())
        p = Person(age)
        p.amIOld()
        for j in range(0, 3):
            p.yearPasses()
        p.amIOld()
        print("")
