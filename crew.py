import csv


with open('crew.csv', encoding= 'utf-8', newline='') as file_object:
    lines = csv.DictReader(file_object)
    for line in lines:
        print(line['ssn'], line['address'])

print(line)



