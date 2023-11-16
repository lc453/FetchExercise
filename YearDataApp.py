import YearlyPredictor
import calendar
import os

file_path=input("Enter the path to the data file in csv format: ")

if os.path.isfile(file_path):
    monthly_predictions=YearlyPredictor.year_predictor(file_path)
    for i, prediction in enumerate(monthly_predictions):
        print("Estimate for " + calendar.month_name[i+1] + " is: " + prediction)
else:
    print("File not found")
    
input("press ENTER to exit")