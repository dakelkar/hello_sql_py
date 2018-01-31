import sqlite3
import csv

conn = sqlite3.connect("test_database.db")
cursor = conn.cursor()
conn.row_factory = sqlite3.Row
all_data = conn.execute('select * from data')
row = all_data.fetchone()
names = row.keys()
f = open('test_database.csv', 'w', newline="")
writer = csv.writer(f,delimiter=',')
writer.writerow(names)
writer.writerows(all_data)
f.close()

