import os 

list_dir = os.listdir()
list_fpies = os.listdir("C:/Users/USUARIO/Desktop/FPIES/Total_FPIES/total_fpies_assoc")

comando  = "gatk CombineGVCFs -R /home/common/references/hg38/Homo_sapiens_assembly38.fasta -D /home/common/references/hg38/Homo_sapiens_assembly38.dbsnp138.vcf.gz "
tail = "-O khor_fpies.g.vcf.gz"

for file in list_dir:
    if not file.endswith(".tgi"):
        flag = ("--variant"+ " gvcfs/"+ file+" ")
        comando = comando + flag
for file in list_fpies:
    if not file.endswith((".pdf",".txt")):
        flag = ("--variant"+ " C:/Users/USUARIO/Desktop/FPIES/Total_FPIES/total_fpies_assoc/"+ file+" ")
        comando = comando + flag
comando = comando + tail
print(comando)

