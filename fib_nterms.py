import sys

from recursion import fibonacci


def main():
    n = input('Print fibonacci numbers upto which nth term?')
    n = int(n)

    for i in range(0, n):
        print(fibonacci(i), end=' ')

    print('\n')


if __name__ == '__main__':
    sys.exit(main())
