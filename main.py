# import modules
import csv
from collections import Counter

# define arrays for rows and columns
rows = []
first_names = []
last_names = []
rlc_event_1 = []
rlc_event_1_team_members = []
rlc_event_2 = []
rlc_event_2_team_members = []

# create array for events
events = []
team_members = []
hashes = []

# define file name
filename = "data.csv"

# open csv file and put the first row into the collumns array
# and the rest of the rows into the rows array
with open(filename, "r") as csvfile:
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

# loop through enumerated rows array

for i, j in enumerate(rows):
    if rlc_event_1[i] == rlc_event_2[i]:
        rlc_event_2[i] = ""
        if rlc_event_2_team_members[i] == rlc_event_1_team_members[i]:
            rlc_event_2_team_members[i] = ""
        else:
            if len(rlc_event_1_team_members[i]) > len(rlc_event_2_team_members[i]):
                rlc_event_2_team_members[i] = ""
            else:
                rlc_event_1_team_members[i] = ""

for i, j in enumerate(rows):
    if rlc_event_1[i] != "":
        # if the rlc_event_1_team_members collumn is not empty
        if rlc_event_1_team_members[i] != "":
            # split the string into a list
            rlc_event_1_team_members[i] = rlc_event_1_team_members[i].split(",")
            for k, l in enumerate(rlc_event_1_team_members[i]):
                # lowercase all entries
                rlc_event_1_team_members[i][k] = l.lower().strip()
            # check if full name is not in the team members list
            if (
                first_names[i].lower().strip() + " " + last_names[i].lower().strip()
                not in rlc_event_1_team_members[i]
            ):
                rlc_event_1_team_members[i].append(
                    first_names[i].lower().strip() + " " + last_names[i].lower().strip()
                )
            rlc_event_1_team_members[i].sort()
            rlc_event_1[i] = rlc_event_1[i].lower().strip()
            # insert the event name into the event_1 array
            rlc_event_1_team_members[i].insert(0, rlc_event_1[i])
            # hash a frozen set of the members + event name to compare against later (in case someone signs up for an event in slot 1
            # and a teammate uses slot 2)
            rlc_1_hash = hash(frozenset(rlc_event_1_team_members[i]))
            if rlc_1_hash not in hashes:
                hashes.append(rlc_1_hash)
                events.append(rlc_event_1[i])
                # add the list to the team_members array
                team_members.append(rlc_event_1_team_members[i])
        else:
            # solo event
            full_name = (
                first_names[i].lower().strip() + " " + last_names[i].lower().strip()
            )
            rlc_event_1_team_members[i] = [full_name]
            rlc_event_1_team_members[i].insert(0, rlc_event_1[i].lower().strip())
            rlc_1_hash = hash(frozenset(rlc_event_1_team_members[i]))
            if rlc_1_hash not in hashes:
                events.append(rlc_event_1[i].lower().strip())
                team_members.append(rlc_event_1_team_members[i])
    else:
        events.append("none")
    ###############################################################################################
    # event 2 logic
    if rlc_event_2[i] != "":
        if rlc_event_2_team_members[i] != "":
            # split the string into a list
            rlc_event_2_team_members[i] = rlc_event_2_team_members[i].split(",")
            for k, l in enumerate(rlc_event_2_team_members[i]):
                # lowercase all entries
                rlc_event_2_team_members[i][k] = l.lower().strip()
            # check if full name is not in the team members list
            if (
                first_names[i].lower().strip() + " " + last_names[i].lower().strip()
                not in rlc_event_2_team_members[i]
            ):
                rlc_event_2_team_members[i].append(
                    first_names[i].lower().strip() + " " + last_names[i].lower().strip()
                )
            rlc_event_2_team_members[i].sort()
            rlc_event_2[i] = rlc_event_2[i].lower().strip()
            rlc_event_2_team_members[i].insert(0, rlc_event_2[i])
            rlc_2_hash = hash(frozenset(rlc_event_2_team_members[i]))
            if rlc_2_hash not in hashes:
                hashes.append(rlc_2_hash)
                events.append(rlc_event_2[i])
                # add the list to the team_members array
                team_members.append(rlc_event_2_team_members[i])
        else:
            full_name = (
                first_names[i].lower().strip() + " " + last_names[i].lower().strip()
            )
            rlc_event_2_team_members[i] = [full_name]
            rlc_event_2_team_members[i].insert(0, rlc_event_2[i].lower().strip())
            rlc_2_hash = hash(frozenset(rlc_event_2_team_members[i]))
            if rlc_2_hash not in hashes:
                events.append(rlc_event_2[i].lower().strip())
                team_members.append(rlc_event_2_team_members[i])
    else:
        events.append("none")

results = Counter(events).most_common()
print(len(Counter(events).keys()), "total events")

# output csv wuith event counts
header = ["Event", "Count"]
with open("out/event_counts.csv", "w") as csvfile:
    write = csv.writer(csvfile)
    write.writerow(header)
    write.writerows(results)

# output csv wuith teams
header = ["Event", "Member #1", "Member #2", "Member #3"]
with open("out/teams.csv", "w") as teamsfile:
    write = csv.writer(teamsfile)
    write.writerow(header)
    write.writerows(team_members)

print(len(team_members), "total teams")
