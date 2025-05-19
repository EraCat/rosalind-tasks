

class Solution:
    def transcribe(self, dna: str) -> str:
        rna = ""
        for i in range(len(dna)):
            if dna[i] == 'T':
                rna += 'U'
            else:
                rna += dna[i]

        return rna

def main():
    s = Solution()
    with open('input.txt', 'r') as file:
        print(s.transcribe(file.read()))


if __name__ == '__main__':
    main()