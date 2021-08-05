import sys


class ArithmeticSequence:
    def __init__(self, first_term, common_difference, num_terms):
        self._sequence_list = []
        self._first_term = first_term
        self._common_difference = common_difference
        self._num_terms = num_terms

        for i in range(1, self._num_terms + 1):
            sequence_term = self._first_term + (i - 1) * self._common_difference
            self._sequence_list.append(sequence_term)
        return

    def sum(self):
        return self._num_terms * self._first_term + (self._num_terms / 2) * (
                self._num_terms - 1) * self._common_difference

    def nth_term(self, n):
        return self._first_term + (n - 1) * self._common_difference

    def show(self):
        for i in self._sequence_list:
            if self._sequence_list.index(i) != len(self._sequence_list) - 1:
                print("%d, " % i, end=" ")
            else:
                print(i)
        return


def main():
    f = input("Enter first term of the sequence:")
    d = input("Enter first common difference of the sequence:")
    n = input("Enter number of terms in the sequence:")

    a1 = ArithmeticSequence(int(f), int(d), int(n))
    a1.show()
    print("Sum of the sequence: %d" % a1.sum())

    t = input("Which term in the sequence do you want to see?")
    print(a1.nth_term(int(t)))


# Call the main()
if __name__ == "__main__":
    sys.exit(main())
