import csv
import os
import event
with open('Gen_key.csv', 'rb') as csvfile:
     data = csv.reader(csvfile,delimiter=' ', quotechar='|')
     for row in data:
       key=''.join(row)
       #os.system("event.py key")
       #print row
       event.main(key)

