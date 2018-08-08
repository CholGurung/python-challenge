import os
import csv
import operator

# Path to collect data from the Resources folder
bankCSV = os.path.join("Resources", "budget_data.csv")
file_output = open("Output//pybank_output.txt","w")

# Function to print monthly change
def calculate_Monthly_Change(lst, n):
    diff = [];
    sum_change = 0
    for i in range(n-1):
        diff.append(lst[i+1] - lst[i])
        sum_change = sum_change + (lst[i+1] - lst[i])

    average_monthly = sum_change / (n-1)
    file_output.write(f'Average  Change: ${average_monthly}' + "\n")
    return diff
     
# Define the function to calculate average
def calculate_Changes(dict_bank):

    dict_change_per_month = []
    keys_list = []
    values = dict_bank.values()
    
    di = dict_bank.items()
    change_list =[]
    for k,v in di:
        change_list.append(int(v))
        keys_list.append(k)
    dict_change_per_month = calculate_Monthly_Change(change_list, len(change_list))
    

# Find the greatest increase in profit over the entire period
    change_dict = zip((x for x in keys_list[1:]),dict_change_per_month)
    monthly_change_dict = dict((x, y) for x, y in set(change_dict))
    max_val = max(dict_change_per_month)
    max_month = [x for x in monthly_change_dict if monthly_change_dict[x] == max_val]
    file_output.write(f'Greatest Increase in Profits: {max_month} (${max_val})' + "\n")

# Find the greatest decrease in losses over the entire period 
    min_val = min(dict_change_per_month)
    min_month = [x for x in monthly_change_dict if monthly_change_dict[x] == min_val]
    file_output.write(f'Greatest Decrease in Profits: {min_month} (${min_val})' + "\n")

# Read in the CSV file
with open(bankCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    net_amount = 0
    total_month = 0
    average_change_between_month = 0
    max_increase_profit = 0
    max_decrease_profit = 0
    dict_bank = dict()
    # Loop through the data
    for row in csvreader:

        net_amount = net_amount + int(row[1])
        total_month = total_month + 1
        dict_bank[row[0]] = row[1]

    
    file_output.write("Financial Analysis" + "\n")
    file_output.write("----------------------------" + "\n")
    file_output.write(f'Total Months: {total_month} ' + "\n")
    file_output.write(f'Total: ${net_amount}' + "\n")
    calculate_Changes(dict_bank)
    file_output.close()