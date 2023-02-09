import pysam

# Create Create an Alignment object
samfile = pysam.AlignmentFile("/path/to/bam/file", "rb")

# Read file with snps
with open("/path/to/file/snps.txt", "r") as file:
	file = file.read()
	for line in file:
		line = line.split(" ")

# Iterating over each base of a specified region
for column in samfile.pileup("chr1", 1, 12794703,truncate = True):
    
	print("\nCoverage at base%s = %s" % (column.pos, column.n))
	for read in column.pileups:
		if not  read.is_del and not read.is_refskip:
			print("\tBase un read %s = %s" % (read.alignment.query_name, read.alignment.query_sequence[read.query_position]))

samfile.close()
