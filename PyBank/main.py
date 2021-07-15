#Importing the necessary modules/libraries
import os, csv

#Creating a variable to csv file path
budget_data = os.path.join("Resources","budget_data.csv")

total_months = 0
net_profit_loss = []
value = []
change = []
#Create empty lists to later append requested values
dates = []
profits = []

#Opening and reading the CSV file
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip header row with next function
    csv_header = next(csvreader)

    #Reading the first row 
    first_row = next(csvreader)
    #total_months += 1
    net_profit_loss = int(first_row[1])
    value = int(first_row[1])
    
    #Loop through each row 
    for row in csvreader:
        dates.append(row[0])
        
        # Calculate the change, then add it to list of changes
        change = int(row[1])-value
        value = int(row[1])
        profits.append(change)
    
        
        #Total number of months
        total_months = (len(dates)) + 1
 
        #Total net amount of "Profit/Losses over entire period"
        net_profit_loss = net_profit_loss + int(row[1])
    #Calculate changes in "Profit/Losses" over the entire period by find difference between greatest 
    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Print Financial analysis
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_profit_loss)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

#Export to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(net_profit_loss)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write(''.format(line1,line2,line3,line4,line5,line6,line7))


