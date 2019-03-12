import os
import csv
votes = 0
candidates = []

# Create dictionary based on print results from unique_candidates variable
cdict = {"Khan": 0 , "Correy" :0 , "Li": 0, "O'Tooley": 0}

csvpath = os.path.join("../Resources", "election_data.csv")

with open(csvpath,newline='') as datafile:
    csvreader = csv.reader(datafile,delimiter=',')
    csvheader = next(csvreader)
    

    for row in csvreader:
        votes += 1
        candidates.append(row[2])

# Create variables for each dictionary key to reference later        
        khancount = cdict["Khan"]
        correycount = cdict["Correy"]
        licount = cdict["Li"]
        otooleycount = cdict["O'Tooley"]

# Add vote totals to dictionary values
        if row[2] == "Khan":
            cdict["Khan"] += 1
        elif row[2] == "Correy":
            cdict["Correy"] += 1
        elif row[2] == "Li":
            cdict["Li"] += 1
        elif row[2] == "O'Tooley":
            cdict["O'Tooley"] += 1
        
# Find percent for each candidate
khanpercent = khancount/votes
correypercent = correycount/votes
lipercent = licount/votes
otooleypercent = otooleycount/votes

# Identify max value from dictionary 
winner = max(cdict.keys(), key=(lambda k: cdict[k]))


output_file = os.path.join("PyPoll.txt")
with open(output_file, "w", newline="") as f:
    print("Election Results")
    print("----------------------------------")
    print(f'Total Votes: {votes}')
    print("----------------------------------")
    print("Khan: "+"{:.2%}".format(khanpercent) + " (" + str(khancount) + ")")
    print("Correy: "+"{:.2%}".format(correypercent) + " (" + str(correycount) + ")")
    print("Li: "+"{:.2%}".format(lipercent) + " (" + str(licount) + ")")
    print("O'Tooley: "+"{:.2%}".format(otooleypercent) + " (" + str(otooleycount) + ")")
    print("----------------------------------")
    print("Winner: " + winner)

    f.write("Election Results"'\n')
    f.write("----------------------------------"'\n')
    f.write(f'Total Votes: {votes}''\n')
    f.write("----------------------------------"'\n')
    f.write("Khan: "+"{:.2%}".format(khanpercent) + " (" + str(khancount) + ")"'\n')
    f.write("Correy: "+"{:.2%}".format(correypercent) + " (" + str(correycount) + ")"'\n')
    f.write("Li: "+"{:.2%}".format(lipercent) + " (" + str(licount) + ")"'\n')
    f.write("O'Tooley: "+"{:.2%}".format(otooleypercent) + " (" + str(otooleycount) + ")"'\n')
    f.write("----------------------------------"'\n')
    f.write(f' Winner: {winner}''\n')
        

# Used these in the first iteration to identify unique set of candidates
    # unique_candidates = set(candidates)
    # print(unique_candidates)





    
