'''Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
Letters_count=0
Digits_count=0
x=input("Enter a sentence:")
for i in range(len(x)):
    if (x[i]>="A" and x[i]<="Z") or (x[i]>="a" and x[i]<="z"):
        Letters_count+=1
    elif(x[i]>="0" and x[i]<="9"):
        Digits_count+=1
print("LETTERS "+str(Letters_count))
print("DIGITS "+str(Digits_count))