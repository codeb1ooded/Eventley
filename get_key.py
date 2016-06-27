import csv
import event

with open('Gen_key.csv', 'rb') as csvfile:
     data = csv.reader(csvfile)
     for row in data:
       key=''.join(row)
       
       #print key

       event.main(key)
       #count=count+1


