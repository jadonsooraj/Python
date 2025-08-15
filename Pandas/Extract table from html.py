#To extract tables from website, copy table tag from inspect element and create a new html file for that table
#extract table using read_html() which returns list of dataframes from that page
#extract your datafram
#convert df.to_csv("new_file_name.csv")
import pandas as pd

tables=pd.read_html('Pandas\orders table.html')
print(tables)

df=tables[0]

df.to_csv("Pandas\orders_table.csv")