import YearlyPredictor
import calendar

print("Enter the path to the data file in csv format: ")
file_path=input()
monthly_predictions=YearlyPredictor.year_predictor(file_path)

for i, prediction in enumerate(monthly_predictions):
    print("Estimate for " + calendar.month_name[i+1] + " is: " + prediction)