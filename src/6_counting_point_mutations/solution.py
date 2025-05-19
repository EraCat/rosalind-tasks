

class Solution:

    def countMutations(self, seq1: str, seq2: str) -> int:
        counter = 0
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                counter += 1

        return counter


def main():
    s = Solution()

    with open('input.txt', 'r') as file:
        print(s.countMutations(file.readline(), file.readline()))


if __name__ == '__main__':
    main()