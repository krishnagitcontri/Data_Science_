# 6. A data.csv file has following data(stateid, name, population in crores, No. of
# Universities)
#   data.csv
# 12001,Gujarat,10,29,12002,Maharashtra,19,36,12003,Rajasthan,13,31,12004,Madhya
# Pradesh,14,21,12005,Punjab,12,13,12006,Karnataka,23,31,12007,Tamilnadu,25,29,1208,
# Keral a,21,15

# Read data.csv file. Transfer data to data structure like following States={
# 12001: {"name":"Gujarat","population":10,"no_of_uni":20},
# 12002: {"name":"Maharashtra","population":19,"no_of_uni":36}
# }
# Using this data, construct dictionary in following manner.

import csv

def dictCsv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        headers = next(reader, None)  # Get the headers from the first line
        states = {}
        for row in reader:
            stateid = int(row[0])
            rest = list(map(int, row[1:]))  # Convert the rest of the row to integers
            states[stateid] = dict(zip(headers[1:], rest))  # Create a dictionary for each state
    return states

states = dictCsv('data.csv')
print(states)