from math import *
import numpy as np
import matplotlib.pyplot as plt
from psm_plot import *

#Put function here -- this should be P'

def lin_fit(x,y):
    n = len(x)
    sumxy = 0.0
    sumx = 0.0
    sumy = 0.0
    sumx2 = 0.0
    sumy2=0.0
    for i in range(0,n):
        sumxy+=x[i]*y[i]
        sumx+=x[i]
        sumy+=y[i]
        sumx2+=pow(x[i],2.0)
        sumy2+=pow(y[i],2.0)

    m = (n*sumxy-sumx*sumy)/(n*sumx2-pow(sumx,2))
    b = (sumx2*sumy-sumxy*sumx)/(n*sumx2-pow(sumx,2.0))
    rxy = (sumxy/n-sumx*sumy/pow(n,2))/sqrt((sumx2/n-pow(sumx/n,2.0))*(sumy2/n-pow(sumy/n,2.0)))
    rxy2 = pow(rxy,2.0)
    return m,b,rxy2

def linear_fit_plot(x,y,n):
    m,b,r2 = lin_fit(x, y)
    x_start = min(x)
    x_end = max(x)
    x_fit = [x_start]
    dx = (x_end-x_start)/n
    y_fit = [m*x_start+b]
    for i in range(1,n):
        x_curr = x_start+i*dx
        x_fit.append(x_curr)
        y_fit.append(m*x_curr+b)

    return (x_fit, y_fit,r2)


x_data = [-2.5, -1.9, -0.9, -0.3, 0.0, 0.3]
y_data = [15.1, 14.03, 13.2, 12.1, 10.99, 9.4]

points = len(x_data)
"""
for x_curr in x_data:
    x.append(x_curr)
    y_curr = b+m*x_curr
    y.append(y_curr)

"""

function_name = "Lin Reg. "
title_base = "Plot of " + function_name
title = title_base
filename = "mod83_lr_.png"
xlabel = "x"
ylabel = "y"
y_func_label = "Linear Regression Fit"

FunctionScatterPlot111(x_data,xlabel,linear_fit_plot,y_func_label,y_data,ylabel,title,filename)



