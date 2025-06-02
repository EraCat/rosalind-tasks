import urllib.request


class Solution:
    n_glycosylation_motif_len = 4
    n_glycosylation_motif_include = ['N', '', ['S', 'T'], '']
    n_glycosylation_motif_exclude = ["", "P", "", 'P']

    def findMotifIndexesAt(self, protein_seq: str) -> list[int]:
        potentials = []
        results = []

        for i in range(len(protein_seq)):
            for j in range(len(potentials) - 1, -1, -1):
                potentials[j]['right'] += 1
                suitable_seq = True
                if len(self.n_glycosylation_motif_include[potentials[j]['right']]) != 0:
                    if protein_seq[i] not in self.n_glycosylation_motif_include[potentials[j]['right']]:
                        suitable_seq = False

                if suitable_seq and len(self.n_glycosylation_motif_exclude[potentials[j]['right']]) != 0:
                    if protein_seq[i] in self.n_glycosylation_motif_exclude[potentials[j]['right']]:
                        suitable_seq = False

                if not suitable_seq:
                    del potentials[j]
                if suitable_seq and potentials[j]['right'] == self.n_glycosylation_motif_len - 1:
                    results.append(potentials[j]['left'] + 1)
                    del potentials[j]

            if protein_seq[i] in self.n_glycosylation_motif_include[0]:
                potentials.append({'left': i, 'right': 0})

        return results


def main():
    s = Solution()
    with open('input.txt', 'r') as file:
        for line in file:
            urlopen = urllib.request.urlopen(f"https://www.uniprot.org/uniprotkb/{line.rstrip().split('_')[0]}.fasta")
            urlopen.readline()
            seq = ''
            for part in urlopen:
                seq += part.decode('utf-8').rstrip()

            indexes = s.findMotifIndexesAt(seq)
            if len(indexes) > 0:
                print(line.rstrip())
                print(' '.join(map(str, indexes)))

if __name__ == '__main__':
    main()
