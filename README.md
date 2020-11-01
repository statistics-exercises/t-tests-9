# Paired comparison tests II

As always let's repeat what we just did in the previous exercise with some slight variations in order to ensure that you have got the idea of what we are doing with these paired comparison tests.

A file called `sales_data.dat` contains two columns of data and 300 rows of data.  Each row in the data set corresponds to one of the salespeople in a large company that sells timeshare apartments.  The first column is the number of timeshare units each individual sold during the year prior to a new marketing drive.  The second column, meanwhile, is the number of timeshare units each individual sold during the year after the marketing drive.  The question the company would like answer did the marketing drive have a net effect (either positive or negative) on sales?

__Your task is to write to perform this paired comparison test.__  Notice that you have __a lot of data points__ in this case.  As always I have provided you with an outline of the functions you should write in order to get you started.  These functions are:

1. `testStatistic` - this function has two arguments `data1` and `data2`.  These are both NumPy arrays with the same length.  The first contains the sales data for the year before the marketing strategy, while the second contains the sales data for the year after the marketing strategy.  This code should calculate and return the test statistic on which the hypothesis test is defined.
2. `pvalue` - this function has two arguments `data1` and `data2`.   These are both NumPy arrays with the same length.  The first contains the sales data for the year before the marketing strategy, while the second contains the sales data for the year after the marketing strategy.   The `pvalue` function should call `testStatistic`.  The value returned from this function should then be used to determine the __p-value__ for the statistical test.
