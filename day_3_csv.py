import csv

fobj = open('csvfile.csv', 'r')
csvobj = csv.DictReader(fobj)

print(csvobj.fieldnames)
headerList = csvobj.fieldnames



#
# print(list(csvobj))

wobj = open('csvout.csv', 'w')

csvwobj = csv.DictWriter(wobj, fieldnames=csvobj.fieldnames,dialect=csv.excel)

header = {}
str1 = 'PASSWORD '
print(str1)
str1 = str1.rstrip().lstrip()
print(type(str1))
print(str1)

for n in csvwobj.fieldnames:
    # n = n.rstrip().lstrip()
    header[n] = n
    print(type(n))
csvwobj.writerow(header)
print(header)

for row in csvobj:
    print(row)
    if row.get('PASSWORD') == 'changeme':
        print('Bad person {}'.format(row.get('FIRST NAME')))
        csvwobj.writerow(row)


# print(help(csv))
