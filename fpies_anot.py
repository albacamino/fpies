
def convert_dict(data_list):
    """
    Convierte una lista en diccionario
    """
    res = {}
    #{_.split("=")[0]: _.split("=")[1] for _ in info_campos}
    for field in data_list:
        nombre, valor = field.split("=")
        res[nombre] = valor
    return res


headers = "CHR \t POS \t ID \t REF \t ALT \t QUAL \t Filter \t AnnoType \t Consequence \t GeneName \t PHRED\n"

with open("total_fpies_annot.txt", "r") as file, open("fpies_annot.txt", "w") as f_out:
    f_out.write(headers)
    
    for line in file:
        if not line.startswith("#"):

            line_split = line.split("\t")
            fields = "\t".join(line_split[:7])
            info = line_split[7].split(";")

            info_dict = convert_dict(info)            
            
            annotype = info_dict["AnnoType"]
            consequence = info_dict["Consequence"]
            genename = info_dict["GeneName"]
            phred = info_dict["PHRED"].split("|")[0]

            f_out.write(f"{fields}\t{annotype}\t{consequence}\t{genename}\t{phred}\n")