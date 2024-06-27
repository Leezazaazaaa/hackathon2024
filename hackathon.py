
import csv

with open('C://Users//user//Downloads//Hackathon2024.csv') as csv_file:
 
        # reading the csv file using DictReader
    csv_reader = csv.DictReader(csv_file)
 
    # converting the file to dictionary
    # by first converting to list
    # and then converting the list to dict
    dict_from_csv = dict(list(csv_reader)[0])
 
    # making a list from the keys of the dict
    list_of_column_names = list(dict_from_csv.keys())
    column_names_string = ''.join(list_of_column_names)
    print(column_names_string)