#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#Import CSV File
import csv
from pathlib import Path

csv_path = Path("Resources/budget_data.csv")

#State the csv file path

#Declared variables
month_Profit_loss = 0
prev_month_profit_loss = 0
profit_loss = []
profit_losses = []

#Calculate the Number of Months
months = []
change_in_profit = []

#Read the csv 
with open(csv_path) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter= ",")

#Don't Include the Header
    next(csvreader)

#Iterate through the remaining rows / extract data from the row
    for row in csvreader:
        date, profit_loss = row[0], int(row[1])
        print(f"Date: {date}, Profit/Loss: {profit_loss}")

#Append the Months
        months.append(date)
        profit_losses.append(profit_loss)
        print(f"Date: {date}, Profit/Loss: {profit_loss}")

#Calculate the change in profit/loss in previous month
        if prev_month_profit_loss !=0:
            change = month_Profit_loss - prev_month_profit_loss
            change_in_profit.append(change)

#Calculate profit and loss
        month_Profit_loss += profit_loss

#store the current month's profit/losses
        prev_month_profit_loss = profit_loss

#Calculate the total number of months
total_months = len(months)
print(total_months)

# Append the profit/loss to the list
profit_losses.append(profit_loss)

#Net total of profit and loss over time 
net_total = sum(profit_losses)
print(net_total)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
average_change = sum(change_in_profit)/len(change_in_profit)
print(round(average_change))

#The greatest increase in profits (date and amount) over the entire period
Greatest_increase = max(change_in_profit)
print(Greatest_increase)
greatest_increase_month = months[change_in_profit.index(Greatest_increase)]

#The greatest increase in profits (date and amount) over the entire period
Greatest_decrease = min(change_in_profit)
print(Greatest_decrease)
greatest_decrease_month = months[change_in_profit.index(Greatest_decrease)]




# print the results
print("Financial Analysis")
print("---")
print(f"Total Months: {total_months} ")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} ${Greatest_increase}")
print(f"Greatest Increase in Losses: {greatest_decrease_month} ${Greatest_decrease}")

# the outputs 
with open("budget_analysis.txt", "w") as textfile: 
    textfile.write("Finacial Analysis\n")
    textfile.write("--------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${profit_loss}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} ${Greatest_increase}\n")
    textfile.write(f"Greatest Increase in Losses: {greatest_decrease_month} ${Greatest_decrease}\n")