from math import *
m = 0
s = 2
x = 1
y = 1/(sqrt(2*pi)*s)*exp((-1/2*(x-m/(s))**2))
print("当m=%d,s=%d,x=%d时,f(x)=%.5f"%(m,s,x,y))
