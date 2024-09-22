import matplotlib.pyplot as plt
import math
import numpy as np

# Graph a single Function in a single Plot
# @params:
# @author: Santino Agosti
def singleGraph(xRange, function, log, xLabel, yLabel, title):
    plt.figure(figsize=(14, 6))
    plt.subplot(1, 2, 1)
    plt.plot(xRange, function)
    if(log == True):
        plt.xscale('log')
    plt.xlabel(f'{xLabel}')
    plt.ylabel(f'{yLabel}')
    plt.title(f'{title}')
    plt.grid(True)

# Define a range of real values. 
# @params:
# @author: Santino Agosti
def realRange(minVal, maxVal, log, samples):
    if(log == True):
        xValues = np.logspace(np.log10(minVal), np.log10(maxVal), samples)  # log scale
    else:
        xValues = np.linspace(minVal, maxVal, samples)  # linear scale
    return xValues