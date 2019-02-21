import baostock as bs
import pandas as pd
import mysql.connector
import time
import datetime
import random
from decimal import Decimal

def process_data(code):
    print(code)
    time.sleep(random.randint(1,5))

    #return
    rs = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,volume,amount,adjustflag,turn,pctChg",
        start_date='2006-01-01', end_date=str(datetime.date.today()),
        frequency="w", adjustflag="1")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)


    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    df = pd.DataFrame(data_list, columns=rs.fields)
    print(df.head(5))

    #result.to_csv("D:\\history_A_stock_k_data.csv", index=False)
    #print(df)

    # mydb = mysql.connector.connect(
    # host="localhost",
    # user="root",
    # passwd="password",
    # database='stock_data'    
    # )
    # mycursor = mydb.cursor()
    # sql = """INSERT INTO `stock_data`.`histories_1`(`date`,
    #         `code`,
    #         `open`,
    #         `high`,
    #         `low`,
    #         `close`,
    #         `preclose`,
    #         `volume`,
    #         `amount`,
    #         `adjustflag`,
    #         `turn`,
    #         `tradestatus`,
    #         `pctChg`,
    #         `peTTM`,
    #         `pbMRQ`,
    #         `psTTM`,
    #         `pcfNcfTTM`,
    #         `isST`)
    #         VALUES
    #         (%s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s,
    #         %s);"""

    # # val = [(date,code,Decimal(open),Decimal(high),Decimal(low),Decimal(close),Decimal(preclose),int(volume),Decimal(amount),int(adjustflag),float(0 if turn=='' else turn),int(tradestatus),Decimal(pctChg),Decimal(peTTM),Decimal(pbMRQ),Decimal(psTTM),Decimal(pcfNcfTTM),int(isST))
    # # for (date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST) 
    # # in (tuple(x) for x in df.values)]
    # val = [tuple(v) for v in df.values]
    # print(val)
    # mycursor.executemany(sql, val)
    # mydb.commit()
    # print(mycursor.rowcount, "was inserted.")


def main():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='stock_data'
    )
    mycursor = mydb.cursor()
    sql = "SELECT code FROM stock_data.stocks;"
    mycursor.execute(sql)


    lg = bs.login()
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    for code in mycursor:
        process_data(code[0])

    print(mycursor.rowcount, "was queried.") 
    mycursor.close()
    mydb.close()

    bs.logout()

if __name__ == "__main__":
    main()


