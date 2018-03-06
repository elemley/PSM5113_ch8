from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *

#Put function here -- this should be P'
def f_linear(x):
    m = -0.5
    b= -5.0
    tmp = m*x+b
    return tmp

def f_quad(x):
    a = 1.0
    b = -2.0
    c = 0.5
    tmp = a*x**2+b*x+c
    return tmp

def f_poly(x):
    a = [-0.1, 3.5, -5.7]
    #, 9.4, -5.6]
    tmp = 0.0
    for i in range(0,len(a)):
        tmp+=a[i]*pow(x,i)
    return tmp

def f_sqrt(x):
    a = 0.3
    b = 1.0
    if x >=0:
        tmp = a*sqrt(b*x)
    else:
        tmp = 999
    return tmp

def f_exp(x):
    #a = 2.718281828459045
    #a = exp(1.0)
    a = 10.0
    P_0 = 1000
    r = -.5
    tmp = P_0*pow(a,r*x)
    return tmp

def f_log(x,b):
    a = 0.5
    tmp = a*log(x,b)
    return tmp

def f_logistic(x):
    P_0 = 1000
    M = 5000
    r = 0.5
    tmp = M*P_0/((M-P_0)*exp(-r*x)+P_0)
    return tmp

def f_trig(x):
    B = 1.0
    a = -pi/2
    tmp = B*sin(a*x)
    return tmp

x_0 = -2*pi
b = exp(1)
#y_0 = f_linear(x_0)
#y_0 = f_quad(x_0)
#y_0 = f_poly(x_0)
#y_0 = f_sqrt(x_0)
#y_0 = f_exp(x_0)
#y_0 = f_log(x_0,b)
#y_0 = f_logistic(x_0)
y_0 = f_trig(x_0)
dx = .1
x = [x_0]
y = [y_0]

x_max = 2*pi
n = int((x_max-x_0)/dx)+1

for i in range(1,n):
    x_curr = x_0 + i*dx
    x.append(x_curr)
    y_curr = f_trig(x_curr)
    y.append(y_curr)

#print sqrt(-1.0)
function_name = "sine Function - ..."
#function_name = "Quadratic Function - y=ax^2+bx+c"
#function_name = "Linear Function - y=mx+b"
title_base = "Plot of " + function_name
title = title_base
filename = "mod82_sin_" + str(dx) + ".png"
xlabel = "x"
#y1_label = "Linear"
ylabel = "y"

LinePlot111(x,y,xlabel,ylabel,title,filename)

