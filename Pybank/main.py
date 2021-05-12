#Import dependencies
import os
import csv


#Define Variables
months = []
profit_loss = []
count_months = 0
net_profit_loss = 0
profit_changes = []
greatest_profit_increase = 0
greatest_profit_decrease = 0
profit_changes_sum = 0
max_increase_date = ""

#Open and Read the CSVfile
#filepath = "/Users/doniatarjam/Python-challenge/Pybank/Resources/budget_data.csv"

filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'budget_data.csv')

with open (filepath, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")  
    # Read the header row first
    csv_header = next(csvfile) 
    for row in csv_reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    


    #count of months
    for month in months:
        count_months+=1
    print("Total months:" + str(count_months))

    #The net total amount of "Profit/Losses" over the entire period
    for amount in profit_loss:
        net_profit_loss = net_profit_loss + amount
    print("Total:" + "$" + str(net_profit_loss)) 

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for x in range(len(profit_loss)-1):
        profit_changes.append(profit_loss[x+1]-profit_loss[x])
    average = round(sum(profit_changes)/(count_months -1),2)
    print("Average of changes: " + "$" + str(average))

    #The greatest increase in profits (date and amount) over the entire period
    greatest_profit_increase = max(profit_changes)
    max_increase_date = months[profit_changes.index(greatest_profit_increase) +1]
    print("Greatest increase in profit: " + max_increase_date + " " + "$" + str(greatest_profit_increase))

    #he greatest decrease in losses (date and amount) over the entire period
    greatest_profit_decrease = min(profit_changes)
    min_increase_date = months[profit_changes.index(greatest_profit_decrease) +1]
    print("Greatest decrease in profit: " + min_increase_date + " " + "$" + str(greatest_profit_decrease))




#An "analysis" folder that contains your text file that has the results from your analysis.
output_file = os.path.join("Analysis", "budget_data.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {count_months}")
    file.write("\n")
    file.write(f"Total: ${net_profit_loss}")
    file.write("\n")
    file.write(f"Average Change: {average}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_increase_date} (${(str(greatest_profit_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_increase_date} (${(str(greatest_profit_decrease))})")
