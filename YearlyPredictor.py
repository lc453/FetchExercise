# import libraries to use
import csv
import numpy as np

def year_predictor(file_string):
    months=[]
    # read the file and insert the data into the array
    with open(file_string) as data_file:
        data_reader = csv.reader(data_file)
        
        # skip the header row
        next(data_reader)
        
        month_data=[]
        month_num=0
        for row in data_reader:
            # determine which month the data is coming from
            date=row[0]
            month=date.split('-')[1]
            # if the month from the date doesn't match what's saved in month_num, we need to start collecting from a new month
            if month != month_num:
                if month_num!=0:
                    months.append(np.array(month_data))
                    month_data=[]
                month_num=month
            month_data.append(int(row[1]))
        
        # the last month still needs to be added to months
        months.append(np.array(month_data))
        
    # Function for retrieving the rate of increase of a month approximated linearly
    def monthly_rate(month):
        # 'A' matrix for linear regression calcuation 
        A = np.vstack([np.array(range(1,len(month)+1)), np.ones_like(month)]).T
        rate, beginning = np.linalg.lstsq(A, month, rcond=None)[0]
        end = beginning + rate*len(month)
        # return the rate relative to the beginning estimate of the month (ending estimate of last month)
        return rate/beginning, end
        
    # Function for calcuating the total receipts for a month based on the estimate
    def total_month(begin, rate, days):
        return days*(rate * days/2 + begin)
            
    # The end of December will be the beginning of january next year
    start_estimate = monthly_rate(months[-1])[1]
    
    monthly_estimates=[]
    for i, month in enumerate(months):
        rate = monthly_rate(month)[0] * start_estimate
        # Can't use the result of montlyrate for the end estimate because that gives estimate from last year's month
        end_estimate = start_estimate + rate*len(month)
        monthly_estimates.append(str(int(np.round(total_month(start_estimate, rate, len(month))))))
        start_estimate = end_estimate
    
    return monthly_estimates
# 