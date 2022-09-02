#MWP Solution
from cmath import cos
from math import sin
x=85
y=-45
Txy=30
i=10
sigx=((x+y)/2)+((x-y)/2)*cos(2*i) + Txy*sin(2*i)
print(sigx)