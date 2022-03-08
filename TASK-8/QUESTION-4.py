lst = [ ]
n = int(input("ENTER THE NUMBER OF ELEMENTS TO BE ADDED IN LIST : "))
for i in range(0, n):
    a = input()
    lst.append(a)
print(lst)

import pandas as pd
series = pd.Series(lst)
print("THE CAPITALIZED FORM :")
for i in series:
    print(i.capitalize(),end=' ')