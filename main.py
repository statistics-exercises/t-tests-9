import numpy as np
import scipy.stats

def testStatistic( data1, data2 ) :
  # Your code to compute the test statistic goes here

  
def pvalue( data1, data2 ) :
  # Your code to calculate the p-value goes here.
  
  
  
# This part of the code does the hypothesis test
data = np.loadtxt("sales_data.dat")
print("The null hypothesis is that the marketting has had")
print("no effect on sales")
print("The alternative hypothsis is that the marketting has had")
print("an effect on sales")
print("The p-value for this hypothesis test is", pvalue(data[0,:], data[1,:]) )
