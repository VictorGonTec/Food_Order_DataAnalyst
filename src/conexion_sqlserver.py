import pyodbc
from decouple import config
import pandas as pd

host=config('SQL_HOST')
database=config('DB')
user=config('USER')
password=config('SQL_PASSWORD')


def connection_db():
  connection=None
  try:
    connection=pyodbc.connect('DRIVER={SQL Server};SERVER='+host+';DATABASE='+database+';UID='+user+';PWD='+password)
  
  except Exception as ex:
    print(ex)
  return connection
 
print(connection_db())
def query_insert(connection,query):
  cursor=connection.cursor()
  try:
    cursor.execute(query)
    connection.commit()
  except Exception as ex:
    print(ex)
  return cursor

def read_query(connection,query):
  cursor=connection.cursor()
  result = None
  try:
    cursor.execute(query)
    result=cursor.fetchall()
    return result
  except Exception as ex:
    print(ex)
  
  

  
query="""
SELECT * FROM food_order;
"""
connection=connection_db()
results=read_query(connection,query)

feature_db=[]
for row in results:
  row = list(row)
  feature_db.append(row)


columns=['order_id','customer_id','restaurant_name','cuisine_type','cost_of_the_order','day_of_the_week','rating','food_preparation_time','delivery_time']

def make_dataframe():
  return pd.DataFrame(feature_db,columns=columns)
