class AdvancedArithmetic(object):
    def divisor_sum(self, n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisor_sum(self, n):
        ret = n
        for i in range(1, n):
            if n % i == 0:
                ret += i
        return ret


if __name__ == '__main__':
    n = int(input())
    my_calculator = Calculator()
    s = my_calculator.divisor_sum(n)
    print("I implemented: " + type(my_calculator).__bases__[0].__name__)
    print(s)
