import os 

list_dir = os.listdir("path/to/dir")
list_fpies = os.listdir("path/to/dir")

comando  = "gatk CombineGVCFs -R /home/common/references/hg38/Homo_sapiens_assembly38.fasta -D /home/common/references/hg38/Homo_sapiens_assembly38.dbsnp138.vcf.gz "

tail = "-O output.vcf.gz"

for file in list_dir:
    if not file.endswith(".tbi"):
        flag = ("--variant" + " path/to/dir/" + file + " ")
        comando = comando + flag

for file in list_fpies:
    if not file.endswith((".pdf",".txt")):
        flag = ("--variant" + " path/to/dir/" + file + " ")

        comando = comando + flag
comando = comando + tail
print(comando)

