# The total number of votes cast

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote

#Import CSV File
import csv
from pathlib import Path
import collections
from collections import Counter

csv_path = Path("Resources/election_data.csv")


#Declared Values 
total_voters = []
votes_per_candidate = []
list_of_candidates = []

#csv_path = Path(r"/Users/kelechionuoha/Desktop/election_data.csv")

#read the CSV
with open(csv_path) as csvfile:    
    csvreader = csv.reader(csvfile, delimiter= ",")

#Don't Include the Header
    next(csvreader)

#Iterate through the remaining rows / extract data from the row
    for row in csvreader:
        total_voters.append(row[2])

#Sort the list
list_of_candidates = sorted(total_voters)        

#Use Counter library to find common elements and count
cleaned_list = Counter(list_of_candidates)

# Need to convert Counter object to list
votes_per_candidate.append(cleaned_list.most_common())

# calc the candidate vote percetnage, 3rd decimal - look at the solution image provided 
    # percentage = ( votes per candidate / number of votes ) * 100 
for item in votes_per_candidate:
    first_place_percetage = format(item[0][1]*100/(sum(cleaned_list.values())), '.3f')
        # .3f return to teh 3rd decimal place 
    second_place_percentage = format(item[1][1]*100/(sum(cleaned_list.values())), '.3f')
    third_place_percentage = format(item[2][1]*100/(sum(cleaned_list.values())), '.3f')

#count the number of total votes
total_voter_count = len(total_voters)
print(total_voter_count)

# print the results like the image 
print("Election Results")
print("---------")
print(f"Total Votes:  {total_voter_count}")
print("---------")
print(f"{votes_per_candidate[0][0][0]}: {first_place_percetage}% ({votes_per_candidate[0][0][1]}\n")
print(f"{votes_per_candidate[0][1][0]}: {second_place_percentage}% ({votes_per_candidate[0][1][1]}\n")
print(f"{votes_per_candidate[0][2][0]}: {third_place_percentage}% ({votes_per_candidate[0][2][1]}\n)")
print("---------")
print(f"Winner: {votes_per_candidate[0][0][0]}")
print("---------")