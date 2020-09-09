import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")


with open (csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

print (f"CSV Header: {csv_header}")

row_count = sum(1 for row in csvreader)

print (row_count)



#print (f'Total Months : {total_months}')
#print(f'Total Profit/Losses : {total_profit_or_loss}')
#print(f'Average Change : {average_profit_and_loss}')
#print(f'Greatest Increase in Profits : {Max_profit_and_loss}')
#print(f'Greatest Decrease in Profits : {Min_profit_and_loss}')


