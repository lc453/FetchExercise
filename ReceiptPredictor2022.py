# import libraries to use
import csv
import numpy as np
import calendar

months=[]
# read the file and insert the data into the array
with open(".\data_daily.csv") as datafile:
    datareader = csv.reader(datafile)
    
    # skip the header row
    next(datareader)
    
    monthdata=[]
    monthnum=0
    for row in datareader:
        # determine which month the data is coming from
        date=row[0]
        month=date.split('-')[1]
        # if the month from the date doesn't match what's saved in monthnum, we need to start collecting from a new month
        if month != monthnum:
            if monthnum!=0:
                months.append(np.array(monthdata))
                monthdata=[]
            monthnum=month
        monthdata.append(int(row[1]))
    
    # the last month still needs to be added to months
    months.append(np.array(monthdata))
    
# Function for retrieving the rate of increase of a month approximated linearly
def monthlyrate(month):
    # 'A' matrix for linear regression calcuation 
    A = np.vstack([np.array(range(1,len(month)+1)), np.ones_like(month)]).T
    rate, beginning = np.linalg.lstsq(A, month)[0]
    end = beginning + rate*len(month)
    # return the rate relative to the beginning estimate of the month (ending estimate of last month)
    return rate/beginning, end
    
# Function for calcuating the total receipts for a month based on the estimate
def totalmonth(begin, rate, days):
    return days*(rate * days/2 + begin)
        
# The end of December will be the beginning of january next year
startEstimate = monthlyrate(months[-1])[1]

for i, month in enumerate(months):
    rate = monthlyrate(month)[0] * startEstimate
    # Can't use the result of montlyrate for the end estimate because that gives estimate from last year's month
    endEstimate = startEstimate + rate*len(month)
    print("Estimate for " + calendar.month_name[i+1] + " is: " + str(int(np.round(totalmonth(startEstimate, rate, len(month))))))
    startEstimate = endEstimate
# 