import os
import csv
months = 0
balance = 0
profitlist = []
changelist = []
monthlist = []

csvpath = os.path.join("../Resources","budget_data.csv")

with open(csvpath, newline='', encoding="utf8") as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    csvheader = next(csvreader)
    

    for row in csvreader:
        months += 1
        profit = int(row[1])
        profitlist.append(profit)
        monthlist.append(row[0])
        balance += profit

        # Starting at month 2 calculate changes against second to last item in profit list
        if months >1:
            change = int(row[1]) - profitlist[len(profitlist)-2]
            changelist.append(change)  
            
        
# Function to identify average of changelist
def average(numbers):
    length = len(changelist)
    total = 0.0
    for change in changelist:
        total += change
    return total / length
        
# find the min and max of the changelist   
increase = max(changelist)
decrease = min(changelist)

#Use index positioning to find month of largest increase and decrease
maxspot = monthlist[changelist.index(increase)+1]
minspot = monthlist[changelist.index(decrease)+1]


output_file = os.path.join("PyBank.txt")
with open(output_file, "w", newline="") as f:
    print("Financial Analysis")
    print("-----------------------------------")
    print(f' Total Months: {months}')
    print(f' Total: $ {balance}')
    print(f' Average Change: {average(changelist)}')
    print(f' Greatest Increase in Profits: {maxspot} {increase}')
    print(f' Greatest Decrease in Profits: {minspot} {decrease}')

    f.write("Financial Analysis"'\n')
    f.write("-------------------------"'\n')
    f.write(f' Total Months: {months}''\n')
    f.write(f' Total: ${balance}''\n')
    f.write(f' Average Change: ${average(changelist)}''\n')
    f.write(f' Greatest Increase in Profits: {maxspot} ${increase}''\n')
    f.write(f' Greatest Decrease in Profits: {minspot} ${decrease}''\n')    

