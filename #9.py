'''
Question£º
Write a program that accepts sequence of lines as input and prints the lines after making 
all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
string=[]
print("Enter the strings in sequence to capitalize")
while True: #To enter string in lines
    s=input()
    if s:
        string.append(s.upper())
    else:
        break
for x in string: #To print in lines
    print(x)