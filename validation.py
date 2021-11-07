#import modules
import csv
from collections import Counter

#define arrays for rows and columns
rows = []
first_names = []
last_names = []
rlc_event_1 = []
rlc_event_1_team_members = []
rlc_event_2 = []
rlc_event_2_team_members = []

#create array for events
events = []
team_members = []
rlc_1_hashes = []
rlc_2_hashes = []

#define file name
filename = "data.csv"

#open csv file and put the first row into the collumns array
# and the rest of the rows into the rows array
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    for row in csvreader:
        rows.append(row)
        first_names.append(row[1])
        last_names.append(row[2])
        rlc_event_1.append(row[6])
        rlc_event_1_team_members.append(row[7])
        rlc_event_2.append(row[8])
        rlc_event_2_team_members.append(row[9])

#combine first and last name arrays to make a full name array
full_names = []
for i in range(len(first_names)):
    full_names.append(first_names[i].lower().strip() + " " + last_names[i].lower().strip())

for i, j in enumerate(rows):
    #if the rlc_event_1_team_members collumn is not empty
    if rlc_event_1_team_members[i] != "":
        rlc_event_1_team_members[i] = rlc_event_1_team_members[i].split(",")
        for k, l in enumerate(rlc_event_1_team_members[i]):
            #lowercase all entries
            rlc_event_1_team_members[i][k] = l.lower().strip()
        #check if full name is not in the team members list
        if first_names[i].lower().strip() + " " + last_names[i].lower().strip() not in rlc_event_1_team_members[i]:
            rlc_event_1_team_members[i].append(first_names[i].lower().strip() + " " + last_names[i].lower().strip())
        rlc_event_1_team_members[i].sort()
        rlc_1_hash = hash(frozenset(rlc_event_1_team_members[i]))
        for name in rlc_event_1_team_members[i]:
            if name not in full_names:
                print(i+2, name + " is not in the full name list")
            else:
                # find the index of the full name in the full name array
                index = full_names.index(name)
                if rlc_event_1_team_members[index] != "":
                    # split the rlc_event_1_team_members collumn into a list if it is not already a list
                    if type(rlc_event_1_team_members[index]) != list:
                        print(rlc_event_1_team_members[index])
                        rlc_event_1_team_members[index] = rlc_event_1_team_members[index].split(",")
                    for a, b in enumerate(rlc_event_1_team_members[index]):
                        print(rlc_event_1_team_members[index])
                        #rlc_event_1_team_members[index][a] = b.lower().strip()
                    #check if full name is not in the team members list
                    if first_names[i].lower().strip() + " " + last_names[i].lower().strip() not in rlc_event_1_team_members[i]:
                        rlc_event_1_team_members[i].append(first_names[i].lower().strip() + " " + last_names[i].lower().strip())
                    rlc_event_1_team_members[i].sort()
                    new_hash = hash(frozenset(rlc_event_1_team_members[i]))
                    if new_hash != rlc_1_hash:
                        print(i+2, name, "The hash of the team members list for RLC 1 is not the same as the hash of the full name list")