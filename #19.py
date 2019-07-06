'''
Question:
A website requires the users to input username and password to register. 
Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. 
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''
CheckPasswordlist=[x for x in input("Enter passwords seperated by commas").split(",")]
ValidPasswordlist=[]
LowercaseCount=0
UppercaseCount=0
DigitsCount=0
Characters=0
for x in CheckPasswordlist:
    
    for i in range(len(x)):
       
        if(x[i]>="A" and x[i]<="Z"):
            UppercaseCount+=1
        elif(x[i]>="a" and x[i]<="z"):
            LowercaseCount+=1
        elif(x[i]>="0" and x[i]<="9"):
            DigitsCount+=1
        elif(x[i]=="$" or x[i]=='#' or x[i]=='@'):
            Characters+=1
        else:
            pass
    if(UppercaseCount>0 and LowercaseCount>0 and DigitsCount>0 and Characters>0 and (len(x)>=6 and len(x)<=12)):
        ValidPasswordlist.append(x)
    LowercaseCount=0
    UppercaseCount=0
    DigitsCount=0
    Characters=0
print(ValidPasswordlist)