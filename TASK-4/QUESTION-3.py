print("CREATING A TABLE AND DISPLAYING SECOND ROW OF THE TABLE;")
print("")
A = [ [21001, "ARUN", 75],
     [21002, "VARUN", 85],
     [21003, "THARUN", 95]]   
print ("{:<10} {:<10} {:<10}".format('Roll No','Name','Marks'))
for B in A:
    Roll, name, marks = B
    print ("{:<10} {:<10} {:<10}".format( Roll, name, marks))
print("")
print("")
print("THE SECOND ROW OF THE TABLE");

import pandas as pd
X = [ [21001, "ARUN", 75],
     [21002, "VARUN", 85],
     [21003, "THARUN", 95]]
print("")
data = pd.DataFrame([21002, "VARUN", 85])
print ("{:<6} {:<6} {:<6}".format('21002','VARUN','85'))