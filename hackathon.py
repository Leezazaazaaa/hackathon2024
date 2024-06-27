
import csv

def convertListToString(file_path):
    
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
   
        dict_from_csv = dict(list(csv_reader)[0])
 

        list_of_column_names = list(dict_from_csv.keys())
        column_names_string = ''.join(list_of_column_names)
        print(column_names_string)

 
        