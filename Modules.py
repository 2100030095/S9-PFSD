#import os
#print(os.name)
#print(os.path)
#print(os.getcwd())
import csv
fields=["Name:","Branch","Cgpa"]
rows=[["Mani","CSE",9.5],["Suresh","EEE",9.2]]
file1="Book1.csv"
with open(file1,'w') as csvfile:
    csvwriter=csv.writer(file1)
    csvwriter.writerow(file1)
    csvwriter.writerows(rows)

