import pandas as pd

html_path='customers.html'
table=pd.read_html(html_path)

#as read_html returns list of tables, hence your first element of list is your required tabble 
df=pd.DataFrame(table[0])
print(df)
df.to_csv("customers table.csv")