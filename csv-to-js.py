import csv

def process(fname, vname):
    with open(fname + ".csv", encoding="utf8") as fin:
        c = csv.reader(fin)
        with open(fname + ".js", "w+", encoding="utf8") as fout:
            fout.write("const " + vname + " = [\n")
            next(c)
            for row in c:
                pattern = row[1].replace("\\", "\\\\")
                fout.write('\t{{ "id":"{}", "exp_string":"{}", "exp":new RegExp("{}") }},\n'.format(row[0], pattern, pattern))
            fout.write("];")

process("namesprofanity", "profanity_rules")
process("namesreserved", "reserved_rules")

    
