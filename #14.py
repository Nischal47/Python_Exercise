'''
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
Count={
    "UpperCase":0,
    "LowerCase":0
}
x=input("Enter a sentence:")
for i in x:
    s=i
    if(s.isupper()):
        Count["UpperCase"]+=1
    elif(s.islower()):
        Count["LowerCase"]+=1
print("UPPER CASE "+str(Count["UpperCase"]))
print("LOWER CASE "+str(Count["LowerCase"]))