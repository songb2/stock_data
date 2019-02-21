import mysql.connector
import tushare as ts



ts.set_token('c5d7069264f4d5433702545cfd0dd72979d065cb8ee84f561c6928d9')
pro = ts.pro_api()
df = pro.daily(trade_date='20190215', fields='ts_code')
print(df.columns)
#df = pro.weekly(trade_date='20181123', ts_code='600000.SH',  fields='ts_code,trade_date,open,high,low,close,vol,amount')
#df = pro.daily_basic(ts_code='600000.SH', trade_date='20190215')

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   passwd="password",
#   database='stock_data'
# )
# mycursor = mydb.cursor()
# sql = "INSERT INTO stocks (code, name) VALUES (%s, %s)"
# val = [(code.lower(), name) for code, name in (tuple(x)+('',) for x in df.values)]
# #val = [tuple(x)+('',) for x in df.values]
# print(val)
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")
