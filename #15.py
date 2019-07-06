'''
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Note:Should work on any equation with similar properties.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
a=int(input("Enter a digit:"))
b=input("How many times to itterate:")
y=0
c=a
for x in range(int(b)):
    y=y+c
    c=int(str(c)+str(a))
print(y)