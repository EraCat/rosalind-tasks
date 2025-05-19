from mypyc.codegen.literals import format_int


class Solution:
    d = {
        'F': 2,
        'L': 6,
        'I': 3,
        'M': 1,
        'V': 4,
        'S': 6,
        'P': 4,
        'T': 4,
        'A': 4,
        'Y': 2,
        'Stop': 3,
        'H': 2,
        'Q': 2,
        'N': 2,
        'K': 2,
        'D': 2,
        'E': 2,
        'C': 2,
        'W': 1,
        'R': 6,
        'G': 4
    }

    _stop_kodon = 'Stop'

    def numberOfPossibleRNA(self, proteins: str) -> int:
        number = 1

        for protein in proteins:
            number = (number * int(self.d[protein])) % 1000000

        number = (number * int(self.d[self._stop_kodon])) % 1000000

        return number


def main():
    s = Solution()

    with open('input.txt') as file:
        print(s.numberOfPossibleRNA(file.read().rstrip()))


if __name__ == '__main__':
    main()