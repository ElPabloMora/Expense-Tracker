import os
import csv
from datetime import datetime
import pandas as pd
import calendar
  
FILENAME = 'expenses.csv'

date = datetime.now()
format_time = date.strftime('%Y-%m-%d')

#✅
def add_expenses(description,amount):
    #Create a boolen if routh exists
    file_exist = os.path.exists(FILENAME)
    existing_data = []
    
    if not file_exist:
        with open(FILENAME, 'w', newline='') as file: #Important newline=''
                writer = csv.writer(file)
                writer.writerow(['Id', 'Amount', 'Description', 'Date']) # Write headers
        
    with open(FILENAME,'r') as file:
        reader = csv.reader(file) #Reading file
        next(reader, None)
        existing_data = list(reader)
  
    #Get the most recent ID. Based on the number of records there are, it is assigned and then one is added
    last_id = int(existing_data[-1][0]) if len(existing_data) >= 1 else 0
 
    new_expense = [last_id + 1, amount, description, format_time]
        
    with open(FILENAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(new_expense)

    print(f'Expense added successfully (ID:{last_id+1})')

#✅       
def delete_expense(id):
    
    df = pd.read_csv(FILENAME)
    
    df_delete = df[df['Id'] != int(id)]
    
    #index=false does is that not save the default index !important
    df_delete.to_csv(FILENAME, index=False)

#✅   
def list_expense():

    df = pd.read_csv(FILENAME, header=0)

    if not df.empty:
         print(df.to_string(index=False, justify='left'))
    else:
        print('No data to show! ')

#✅
def sumamry():

    df = pd.read_csv(FILENAME, header=0)
    ets = 0
    for x in df['Amount']:
        ets = ets + x
    print(f'Total expenses: ${ets}')

#✅
def sumamry_month(month):

    df = pd.read_csv(FILENAME, header=0)
    ets = 0
    #The index is very important since with iterrows we are going to iterate each row of the DataFrame
    for index,row in df.iterrows():
        if datetime.strptime(row['Date'],"%Y-%m-%d").month == month:
            ets += row['Amount']
    print(f'Total expenses for {calendar.month_name[month]}: ${ets}')
    
    


