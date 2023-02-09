import pysam
import collections
from tabulate import tabulate

def edit_dicc(bases):
    """
    Agrupa las bases y el número de veces que se lee esa base
    """
    letters = ()
    for k, v in bases.items():
        letter = (k, v)
        letters = letters + letter
    return letters


def bam_pileup(samfile, chrom, pos):

    start = pos
    end = pos + 1

    for pileupcolumn in samfile.pileup(
            "chr" + chrom, start, end, truncate=True):
        coverage = pileupcolumn.n
        bases = pileupcolumn.get_query_sequences(
            mark_matches=False, mark_ends=False, add_indels=False)
        bases = [_.upper() for _ in bases]
        bases = collections.Counter(bases)

        seq = edit_dicc(bases)

        for pileupread in pileupcolumn.pileups:
            if not pileupread.is_del and not pileupread.is_refskip:
                return [chrom, pos, coverage, seq]


if __name__ == "__main__":
    
    import sys
    print(sys.argv)
    samfile = pysam.AlignmentFile(sys.argv[1], "rb")
    headers = ["Chr", "Position", "Coverage", "Bases"]

    with open("/path/to/file/snps/rares.txt", "r") as file:
        result = []
        for line in file:
            chrom, pos = line.split(" ")
            column = bam_pileup(samfile, chrom, int(pos))
            if column is not None:
                result.append(column)
        print(tabulate(result, headers, tablefmt="orgtbl"))
