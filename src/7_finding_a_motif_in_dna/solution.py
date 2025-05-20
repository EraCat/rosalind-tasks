class Solution:

    def findAllMotifs(self, dna: str, pattern: str) -> list[int]:
        potentials = []
        result = []
        for i in range(len(dna)):
            for j in range(len(potentials) - 1, -1, -1):
                if potentials[j]['right'] == len(pattern) - 1:
                    result.append(potentials[j]['left'] + 1)
                    del potentials[j]
                    continue

                potentials[j]['right'] += 1
                if dna[i] != pattern[potentials[j]['right']]:
                    del potentials[j]

            if dna[i] == pattern[0]:
                potentials.append({'left': i, 'right': 0})

        return result


def main():
    s = Solution()
    with open('input.txt', 'r') as file:
        print(' '.join(map(str, s.findAllMotifs(file.readline().rstrip(), file.readline().rstrip()))))


if __name__ == '__main__':
    main()
