from statistics import mean, stdev
import numpy as np
import matplotlib.pyplot as plt


#xData = [1.3, 2, 1.7, 1.5, 1.6, 1.2, 1.6, 1.4, 1, 1.1]
#yData = [10, 6, 5, 12, 10, 15, 5, 12, 17, 20]

xData = [5,	12,	14,	16,	23,	30,	40,	48,	55,	67,	72,	85,	96,	112,	127]
yData = [4,	10,	13,	14,	15,	25,	27,	46,	38,	46,	53,	70,	82,	99,	105]

# Dispersion diagram

plt.scatter(xData,yData)
plt.show()

# Mean
xMean = mean(xData) 
yMean = mean(yData) 

# Std Deviation
xstDev = stdev(xData) 
ystDev = stdev(yData) 

# Linear regression equation formula 

r = np.corrcoef(xData, yData)
print(r)
b = r[0,1]*(ystDev/xstDev)
a = yMean-(b*xMean)

print(a)
print(b)
