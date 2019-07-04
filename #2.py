#Question:
'''Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
'''
x=int(input("Enter a number:"))
i=1
y=1
if x==0:
    y=1
else:
    while i<=x:
        y=y*i
        i=i+1
print("The fatcorial is:",y)
