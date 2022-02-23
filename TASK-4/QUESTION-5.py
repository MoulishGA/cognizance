print("PRINTING THE GIVEN PATTERNED TRIANNGLE;")
A=5
B=A-1
for i in range(0, A):
     for j in range(0, B):
            print(end=" ")
     B = B - 1
     for j in range(0, i+1):
         print("* ", end="")
     print("\r")