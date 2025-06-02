class Solution:
    rabbits = [1, 1]

    def numRabbits(self, months: int, factor: int) -> int:
        for i in range(2, months):
            self.rabbits.append(self.rabbits[i-1] + self.rabbits[i-2] * factor)

        return self.rabbits[months-1]

def main():
    s = Solution()

    print(s.numRabbits(32, 2))


if __name__ == '__main__':
    main()
