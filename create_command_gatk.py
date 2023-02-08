import os

import config

list_dir = os.listdir("path/to/dir")
list_fpies = os.listdir("path/to/dir")

comando = f"gatk CombineGVCFs -R {config.homo_sapiens} -D {config.db_snp}"

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
