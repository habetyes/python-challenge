import os
import csv
votes = 0
cdict = {}

csvpath = os.path.join("../Resources", "election_data.csv")

with open(csvpath,newline='') as datafile:
    csvreader = csv.reader(datafile,delimiter=',')
    csvheader = next(csvreader)    

    for row in csvreader:
        votes += 1
        
        if row[2] not in cdict:
            cdict[row[2]] = 0
        
# Add vote totals to dictionary values
        cdict[row[2]] += 1
       
# Identify max value from dictionary 
winner = max(cdict.keys(), key=(lambda k: cdict[k]))

print("Election Results")
print("--------------------")
print(f'Total Votes: {votes}')
print("--------------------")
for key,value in cdict.items():
    print(f'{key} {value} {(value/votes)*100:.2f}%')
print("--------------------")
print(f'Winner: {winner}')

# Write to File
with open("Pypoll.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("--------------------", file=text_file)
    print(f'Total Votes: {votes}', file=text_file)
    print("--------------------", file=text_file)
    for key,value in cdict.items():
        print(f'{key} {value} {(value/votes)*100:.2f}%' , file=text_file)
    print("--------------------", file=text_file)
    print(f'Winner: {winner}' , file=text_file)






    
