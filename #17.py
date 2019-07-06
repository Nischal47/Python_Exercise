'''
Write a program that computes the net amount of a bank account based a transaction log from console input. 
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
Balance=0
while True:
    transaction=input("Enter transaction ammount starting with D for deposit and W for withdrawl And amount and symbol is seperated by space:")
    if(not transaction):
        break
    transactionlist=transaction.split(" ")
    if(transaction[0]=="D"):
        Balance+=int(transactionlist[1])
    elif(transaction[0]=="W"):
        Balance-=int(transactionlist[1])
    else:
        pass
print("Net Ammount is "+str(Balance))
    
        
