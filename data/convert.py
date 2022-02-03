from email import charset
import country_converter as coco
import csv

cc = coco.CountryConverter()

results = [["count","c1","c2","journal","category"]]
with open('data/collsql.csv', mode='r', encoding="latin1") as file:   
    csvFile = csv.DictReader(file, delimiter = ";")
    for line in csvFile:
        print(line)
        c1c2 = cc.convert(names = [line["Country 1"], line["Country 2"]], to = 'ISO3')
        print(c1c2)
        results.append([line["count(Paper)"], c1c2[0], c1c2[1], line["Journal"], line["Category"]])

with open("res.csv", 'w') as csvfile: 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerows(results)     