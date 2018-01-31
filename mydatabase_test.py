import sqlite3
import os.path
new = "y"
if (os.path.isfile('test_database.db')):
    create = False
else:
    create = True
while (new == "y"):
    conn = sqlite3.connect("test_database.db")
    cursor = conn.cursor()
    if (create):
        cursor.execute("""CREATE TABLE data
                      (PatientID, Center, subytpe, 
                       No_of_blocks, Received_NACT) 
                  """)
    print ("Please enter new record")
    patientid = input("PatientID: " )
    center = input("Center: " )
    subtype = input ("Subtype: ")
    blocks = input ("Number of blocks: ")
    nact = input ("Recieved NACT: ")
    new_data = patientid, center, subtype, blocks, nact
    cursor.execute('INSERT INTO data(PatientID, Center, subytpe, No_of_blocks, Received_NACT) VALUES(?, ?, ?, ?,?)',new_data)
    conn.commit()
    print ("Enter next record?")
    new = input ("y/n: ")
conn.close()

