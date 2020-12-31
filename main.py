import codecs
import csv
import urllib.request

from extended_list import ExtendedList

iris_lst = []

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
stream = urllib.request.urlopen(url)
csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))

# file = open(csv_file)
for line in csv_file:
    iris_lst.append(ExtendedList(line))

iris_lst.pop(0)
for elem in iris_lst:
    print(elem.lst)