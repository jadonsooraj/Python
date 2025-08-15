import os
import pandas as pd
import datetime

def extract_url_table(input_url,folder_path=os.getcwd()):

    import pandas as pd
    import datetime

    url = input_url

    # Assign the table data to a Pandas dataframe
    table = pd.read_html(url)[0]

    # Print the dataframe
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
    
    new_excel_file=os.path.join(folder_path,"Excel_Table_Output_"+time_stamp+".xlsx")

    writer = pd.ExcelWriter(new_excel_file, engine='openpyxl')

    table.to_excel(writer,sheet_name="Output")
    
    writer.close()


    print("Table in Url Converted to Excel File and stored in.." ,new_excel_file)

extract_url_table("https://trends.builtwith.com/websitelist/Responsive-Tables")