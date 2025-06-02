





class Solution:

    def gcContent(self, dna: str) -> float:
        gc_num = 0
        for c in dna:
            if c =='C' or c == 'G':
                 gc_num+= 1

        return (gc_num / len(dna) )* 100


def main():
    s = Solution()

    with open('input.txt', 'r') as file:
        seq = ''
        max = 0
        nameMax = ''
        tempName = ''
        for line in file:
            line = line.rstrip()
            if line.startswith('>'):
                if len(seq) != 0:
                    gc = s.gcContent(seq)
                    if gc > max:
                        max = gc
                        nameMax = tempName
                tempName = line
                seq = ''
            else:
                seq+=line
        if len(seq) != 0:
            gc = s.gcContent(seq)
            if gc > max:
                max = gc
                nameMax = tempName

        print(nameMax)
        print(max)


if __name__ == '__main__':
    main()