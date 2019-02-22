import baostock as bs
import pandas as pd
import datetime
import mysql.connector


lg = bs.login()

print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)
day = str(datetime.date.today())
rs = bs.query_all_stock(day=day)
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)


data_list = []
while (rs.error_code == '0') & rs.next():
    data_list.append(rs.get_row_data())
df = pd.DataFrame(data_list, columns=rs.fields)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database='stock_data'
)
mycursor = mydb.cursor()
sql = """INSERT INTO `stock_data`.`all_stock`
(`code`,
`trade_status`,
`code_name`)
VALUES
(%s, %s, %s) ON DUPLICATE KEY UPDATE code=VALUES(code),trade_status=VALUES(trade_status),code_name=VALUES(code_name);"""
val = [tuple(x) for x in df.values]
print(val)
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

bs.logout()