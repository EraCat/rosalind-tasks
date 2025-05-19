
class Solution:

    # Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s
    def countDNANucleotides(self, seq: str) -> str:
        a = 0
        c = 0
        g = 0
        t = 0
        for nucleotide in seq:
            if nucleotide == 'A':
                a += 1
            if nucleotide == 'C':
                c+=1
            if nucleotide == 'G':
                g +=1
            if nucleotide == 'T':
                t+=1

        return f"{a} {c} {g} {t}"



def main():
    s = Solution()

    with open("input.txt", "r") as f:
        print("Test 1: ", s.countDNANucleotides(f.read()))

if __name__ == "__main__":
    main()