'''
Question:
Write a program that accepts a sequence of whitespace separated words as input and 
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
string=input("Enter string for removing duplicates and sorting seperated by whitespaces:")
thislist=[x for x in string.split(" ")]
thislist=sorted(list(set(thislist)))
for x in thislist:
    print(x,end=" ")