
import pandas as pd
 
df = pd.read_csv('data.csv')
 
list_of_column_names = list(df.columns)
column_names_string = ''.join(list_of_column_names)
print(column_names_string)