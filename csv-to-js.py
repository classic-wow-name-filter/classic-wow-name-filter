import csv

with open("namesprofanity.csv", encoding="utf8") as fin:
    c = csv.reader(fin)
    with open("namesprofanity.js", "w+", encoding="utf8") as fout:
        fout.write("const csv_rules = [\n")
        next(c)
        for row in c:
            pattern = row[1].replace("\\", "\\\\")
            fout.write('\t{{ "id":"{}", "exp_string":"{}", "exp":new RegExp("{}") }},\n'.format(row[0], pattern, pattern))
        fout.write("];")
    
