print("ENTER A NUMBER TO CHECK WHEATHER THE GIVEN NUMBER IS A PALINDROME OR NOT; ")
str=input("ENTER THE NUMBER : ")
rev=str[::-1]
if str==rev:
    print("TRUE")
else:
    print("FALSE")    