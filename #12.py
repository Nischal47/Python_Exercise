'''
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each
 digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
even=[]
for x in range(1000,3001):
   s=str(x)
   if((int(s[0])%2==0)and(int(s[1])%2==0)and(int(s[2])%2==0)and(int(s[3])%2==0)):
       even.append(s)

print(','.join(even))