class Solution:

    def dominantAlleleProbability(self, k: int, m: int, n: int) -> float:
        population_number = k + m + n

        total = population_number * (population_number - 1) / 2

        probability = 0

        # homozygous dominant
        probability += (k * (k - 1)) / 2
        probability += k * m
        probability += k * n

        # heterozygous
        probability += ((m * (m - 1)) / 2) * 0.75
        probability += m * n * 0.5
        # homozygous recessive
        probability += n * (n - 1) / 2 * 0

        return probability / total


def main():
    s = Solution()

    with open('input.txt', 'r') as file:
        split = file.read().split()
        print(s.dominantAlleleProbability(int(split[0]), int(split[1]), int(split[2])))


if __name__ == '__main__':
    main()
