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
        total_votes + = 1
print(f'{total_votes}')