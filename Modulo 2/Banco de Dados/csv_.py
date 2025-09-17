import csv

with open ("dadoss.csv","a", newline="") as arquivo:
    musico = csv.writer(arquivo)
    musico.writerow(["camaro","950","2019","66000"])
