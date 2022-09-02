#MWP Solution
from math import cos
from math import sin
import math

x=85 #value of singma x
y=-45 #value of sigma y
Txy=30 #value of tau xy
for j in range (5,185,5):
    i=math.radians(j) #value of theta

    sigx=((x+y)/2)+(((x-y)/2)*cos(2*i)) + Txy*sin(2*i)
    sigy=((x+y)/2)-(((x-y)/2)*cos(2*i)) - Txy*sin(2*i)
    Txyd=((((y-x)/2)*sin(2*i))+(Txy*cos(2*i)))
    print("values of sigma x' y' and Tx'y' for theta = {} ".format(j))
    print(sigx)
    print(sigy)
    print(Txyd)
