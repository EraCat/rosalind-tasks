class Solution:

    def calculate_expected_offspring(self, genotype_representative_numbers: list[int]) -> int:
        probability = 0
        probability += genotype_representative_numbers[0] * 2
        probability += genotype_representative_numbers[1] * 2
        probability += genotype_representative_numbers[2] * 2
        probability += genotype_representative_numbers[3] * 1.5
        probability += genotype_representative_numbers[4] * 1
        probability += genotype_representative_numbers[5] * 0

        return probability


def main():
    s = Solution()

    input = "18340 16620 16849 17793 18442 17592".rstrip()
    print(s.calculate_expected_offspring(list(map(int, input.split(' ')))))



if __name__ == '__main__':
    main()