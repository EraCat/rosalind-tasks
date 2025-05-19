

class Solution:
    def complementDNA(self, dna: str) -> str:
        result = ""
        for i in  dna[::-1]:
            if i == 'A':
                result += 'T'
            if i == 'T':
                result += 'A'
            if i == 'C':
                result += 'G'
            if i == 'G':
                result += 'C'

        return result

def main():

    s = Solution()
    with open('input.txt', 'r') as file:
        print(s.complementDNA(file.read()))


if __name__ == '__main__':
    main()