import codecs
import csv
import urllib.request

from extended_list import ExtendedList
from connect_db import *

iris_lst = []

url = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
stream = urllib.request.urlopen(url)
csv_file = csv.reader(codecs.iterdecode(stream, 'utf-8'))

# file = open(csv_file)
for line in csv_file:
    iris_lst.append(ExtendedList(line))

iris_lst.pop(0)
iris_lst2 = []
for elem in iris_lst:
    lst2 = []
    it = iter(ExtendedList.next_val(elem.lst))
    while True:
        try:
            lst2.append(next(it))
        except StopIteration:
            break
    iris_lst2.append(ExtendedList(lst2))

    # insert(tuple(lst2))
select_all()
