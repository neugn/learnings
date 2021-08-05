

from recursion import fibonacci
import sys


def main():
    n = input('Upto which number do you want to print all fibonacci numbers? ')
    n = int(n)

    x = 0
    while True:
        fib_series_term = fibonacci(x)
        if fib_series_term > n:
            break
        else:
            print(fib_series_term, end=' ')
            x = x + 1
    print('\n')


if __name__ == '__main__':
    sys.exit(main())
