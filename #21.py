'''
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT 
with a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. 
Please write a program to compute the distance from current position after a sequence of movement and original point. 
If the distance is a float, then just print the nearest integer.
Example:
'''
import math
Org_Pos=[0,0]


while True:
    s=(input("Enter movement of robot as UP, DOWN, LEFT, RIGHT followed by length:"))
    if(not s):
        break
    inputlist=s.split(' ')
   
    direction = inputlist[0]
    steps = int(inputlist[1])
    if(direction=="UP"):
        Org_Pos[1]+=steps
    elif(direction=="DOWN"):
        Org_Pos[1]-=steps
    elif(direction=="LEFT"):
        Org_Pos[0]-=steps
    elif(direction=="RIGHT"):
        Org_Pos[0]+=steps
    else:
        pass
distance=int(math.sqrt(Org_Pos[0]**2+Org_Pos[1]**2))
print("The distance covered by robot is:{}".format(distance))
            