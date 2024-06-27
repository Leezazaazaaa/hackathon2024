
import csv

def convertCsvToList(file_path):

    with open('C://Users//user//Downloads//Hackathon2024.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
   
        dict_from_csv = dict(list(csv_reader)[0])
 

        list_of_column_names = list(dict_from_csv.keys())
        print(list_of_column_names)
        return list_of_column_names
        


    
    

 
        