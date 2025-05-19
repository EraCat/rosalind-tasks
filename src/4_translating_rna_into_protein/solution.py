






class Solution:
    # UUU F      CUU L      AUU I      GUU V
    # UUC F      CUC L      AUC I      GUC V
    # UUA L      CUA L      AUA I      GUA V
    # UUG L      CUG L      AUG M      GUG V
    # UCU S      CCU P      ACU T      GCU A
    # UCC S      CCC P      ACC T      GCC A
    # UCA S      CCA P      ACA T      GCA A
    # UCG S      CCG P      ACG T      GCG A
    # UAU Y      CAU H      AAU N      GAU D
    # UAC Y      CAC H      AAC N      GAC D
    # UAA Stop   CAA Q      AAA K      GAA E
    # UAG Stop   CAG Q      AAG K      GAG E
    # UGU C      CGU R      AGU S      GGU G
    # UGC C      CGC R      AGC S      GGC G
    # UGA Stop   CGA R      AGA R      GGA G
    # UGG W      CGG R      AGG R      GGG G

    d = {
        'UUU' : 'F', #Phenylalanine
        'UUC' : 'F',
        'UUA' : 'L', #Leucine
        'UUG' : 'L',
        'CUU' : 'L',
        'CUC' : 'L',
        'CUA' : 'L',
        'CUG' : 'L',
        'AUU' : 'I', # Isoleucine
        'AUC' : 'I',
        'AUA' : 'I',
        'AUG' : 'M', #Methionine (start)
        'GUU' : 'V', #Valine
        'GUC' : 'V',
        'GUA' : 'V',
        'GUG' : 'V',
        'UCU' : 'S', #Serine
        'UCC' : 'S',
        'UCA' : 'S',
        'UCG' : 'S',
        'CCU' : 'P', #Proline
        'CCC' : 'P',
        'CCA' : 'P',
        'CCG' : 'P',
        'ACU' : 'T', #Threonine
        'ACC' : 'T',
        'ACA' : 'T',
        'ACG' : 'T',
        'GCU' : 'A', #Alanine
        'GCC' : 'A',
        'GCA' : 'A',
        'GCG' : 'A',
        'UAU' : 'Y', # Tyrosine
        'UAC' : 'Y',
        'UAA' : 'Stop',
        'UAG' : 'Stop',
        'CAU' : 'H', # Histidine (b)
        'CAC' : 'H',
        'CAA' : 'Q', #Glutamine
        'CAG' : 'Q',
        'AAU' : 'N', # Asparagine
        'AAC' : 'N',
        'AAA' : 'K', #Lysine
        'AAG' : 'K',
        'GAU' : 'D', #Aspartic acid
        'GAC' : 'D',
        'GAA' : 'E', # Glutamic acid
        'GAG' : 'E',
        'UGU' : 'C', # Cysteine
        'UGC' : 'C',
        'UGA' : 'Stop',
        'UGG' : 'W', #Tryptophan (np)
        'CGU' : 'R', # Arginine
        'CGC' : 'R',
        'CGA' : 'R',
        'CGG' : 'R',
        'AGU' : 'S', # Serine
        'AGC' : 'S',
        'AGA' : 'R', # Arginine
        'AGG' : 'R',
        'GGU' : 'G', #Glycine
        'GGC' : 'G',
        'GGA' : 'G',
        'GGG' : 'G',
    }

    _start_kodon = 'AUG'
    _stop_kodon = 'Stop'

    def translate(self, rna: str) -> str:
        proteins = ''
        begin = rna.find(self._start_kodon)
        if begin == -1:
            return proteins

        while begin < len(rna):
            frame = rna[begin:begin+3]
            begin += 3
            protein = self.d[frame]
            if protein == self._stop_kodon:
                break
            proteins += protein

        return proteins


def main():
    s = Solution()

    with open('input.txt', 'r') as file:
        print(s.translate(file.read()))


if __name__ == '__main__':
    main()