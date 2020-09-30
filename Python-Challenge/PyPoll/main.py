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






print(f"{candidate_list}")
print(f'{total_votes}')