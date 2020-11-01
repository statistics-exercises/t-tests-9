import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_testStatistic(self) : 
        difference = data[0,:] - data[1,:]
        mean = sum(difference) / len(difference) 
        sig = ( len(difference) / (len(difference) - 1 ) )*( sum(difference*difference) / len(difference) - mean*mean )
        stat = mean  / np.sqrt( sig / len(difference) )
        self.assertTrue( np.abs( stat - testStatistic( data[0,:], data[1,:]) )<1e-7, "the function to compute the test statistic is not correct" )
        
    def test_testStatII(self) : 
        difference = data[1,:] - data[0,:]
        mean = sum(difference) / len(difference) 
        sig = ( len(difference) / (len(difference) - 1 ) )*( sum(difference*difference) / len(difference) - mean*mean )
        stat = ( mean ) / np.sqrt( sig / len(difference) )
        self.assertFalse( np.abs( stat - testStatistic( data[0,:], data[1,:] ) )<1e-7, "Your function to compute the test statistic is incorrect as you have the data in the wrong order.  In this case, a POSITIVE test result would indicate that the null hypothesis should be rejected, which is at odds with the information in the description." )
        
    def test_pvalue(self) : 
        stat = testStatistic( data[0,:], data[1,:] )
        if stat<0 : pval = 2*scipy.stats.norm.cdf(stat)
        else : pval = 2*scipy.stats.norm.cdf(-stat)
        self.assertTrue( np.abs( pval - pvalue( data[0,:], data[1,:] ) )<1e-7, "The function you have written to compute the p-value is not correct" )
        
    def test_pvalue2(self) :
        stat = testStatistic( data[0,:], data[1,:] )
        if stat<0 : pval = 2*scipy.stats.t.cdf(stat,len(data[0,:])-1)
        else : pval = 2*scipy.stats.t.cdf(-stat,len(data[0,:])-1)
        self.assertFalse( np.abs( pval - pvalue( data[0,:], data[1,:] ) )<1e-7, "The function you have written to compute the p-value is not correct.  The number of data points here is very large so you can safely use the normal distribution instead of the t-distribution" )
