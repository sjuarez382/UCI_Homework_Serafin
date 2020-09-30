import os
import csv 

# path to collect data 
pypoll_csv = os.path.join('..', 'csv_files', 'election_data.csv')

#declaring all my variables

total_votes = 0
candidate_list = []
Vote_list = []

#reading the file
with open(pypoll_csv) as csvfile:

#checking header
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header:{csv_header}")

#total votes
    for row in csv.reader(csvfile):
        total_votes += 1


#list of candidates
        candidate = (row[2])
        if candidate in candidate_list:
            candidate_index = candidate_list.index(candidate)
            Vote_list[candidate_index] = Vote_list[candidate_index] + 1
        else:
            candidate_list.append(candidate)
            Vote_list.append(1)

#declaring other variables
percent = []
max_index = 0
max_vote = Vote_list[0]

#percent calculations!
for i in range(len(candidate_list)):
    percent_of_votes = round(Vote_list[i] / total_votes*100,2)
    percent.append(percent_of_votes)

    if Vote_list[i] > max_vote:
        max_vote = Vote_list[i]
        print(max_vote)
        max_index = i

#winner winner, chicken dinner
election_winner = candidate_list[max_index]



#printing results
print(f"{candidate_list}")
print(f'{total_votes}')
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]} : {percent[i]}% ({Vote_list[i]})")
print(f'{election_winner}')