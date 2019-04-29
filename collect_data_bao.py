import baostock as bs
import pandas as pd
import mysql.connector
import time
import datetime
import random
from decimal import Decimal

def batch_insert_data(df,table_name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='stock_data'    
    )
    mycursor = mydb.cursor()
    sql = """INSERT INTO `stock_data`.`{0}`(`date`,
            `code`,
            `open`,
            `high`,
            `low`,
            `close`,
            `preclose`,
            `volume`,
            `amount`,
            `adjustflag`,
            `turn`,
            `tradestatus`,
            `pctChg`,
            `peTTM`,
            `pbMRQ`,
            `psTTM`,
            `pcfNcfTTM`,
            `isST`)
            VALUES
            (%s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s);""".format(table_name)

    val = [tuple(v) for v in df.values]
    print(val)
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "was inserted.")

def process_data(code, start_date, end_date, adjust_flag, table_name):
    print(code)
    #end_date = str(datetime.date.today())
    rs = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
        start_date=start_date, end_date=end_date,
        frequency="d", adjustflag=adjust_flag)
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    data_list = []
    while (rs.error_code == '0') & rs.next():
        data_list.append(rs.get_row_data())
    if len(data_list) == 0:
        print('No data between {0} and {1} for {2}'.format(start_date, end_date, code))
        return

    df = pd.DataFrame(data_list, columns=rs.fields)
    batch_insert_data(df,table_name)

def get_start_date(table_name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='stock_data'    
    )

    sql_sdate = "SELECT MAX(date) FROM stock_data.{0};".format(table_name)
    mycursor = mydb.cursor()
    mycursor.execute(sql_sdate)
    myresult = mycursor.fetchone()
    s_date = myresult[0]
    if s_date==None:
        return ''
    #start_date = str((s_date + datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    return s_date

def get_start_date_from_import_data_history(table_name):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='stock_data'    
    )

    sql_sdate = "SELECT MAX(end_date) FROM stock_data.import_data_history where table_name='{0}';".format(table_name)
    mycursor = mydb.cursor()
    mycursor.execute(sql_sdate)
    myresult = mycursor.fetchone()
    s_date = myresult[0]
    if s_date==None:
        return ''
    #start_date = str((s_date + datetime.timedelta(days=1)).strftime('%Y-%m-%d'))
    return s_date

def insert_data_to_import_data_history(tb_name, start_date, end_date):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='stock_data'    
    )
    mycursor = mydb.cursor()
    #sql = "INSERT INTO `stock_data`.`import_data_history`(`table_name`, `start_date`, `end_date`) VALUES ('%s', '%s', '%s');" % (tb_name, start_date, end_date)
    sql = "INSERT INTO `stock_data`.`import_data_history`(`table_name`, `start_date`, `end_date`) VALUES (%s, %s, %s);"
    val = (tb_name, start_date, end_date)
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except Exception as ex:
        print(ex)
        mydb.rollback()
    finally:
        mydb.close()
    

def main():
    lg = bs.login()
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    for adjust_flag in ['1','2','3']:
        table_name = 'histories_{0}'.format(adjust_flag)

        start_date_max = get_start_date(table_name)
        # try to get start_date from table import_data_history
        start_date_import = get_start_date_from_import_data_history(table_name)
        start_date = start_date_import 

        # if result is null, set start_date to be '2006-01-01' and end_date to be today; insert to table import_data_history

        if start_date_import == '' and start_date_max == '':
            start_date = datetime.date(2006, 1, 1)
        elif start_date_import == '' and start_date_max != '':
            start_date = start_date_max
        elif start_date_import != '' and start_date_max == '':
            start_date = datetime.date(2006, 1, 1)
        elif start_date_import > start_date_max:
            start_date = start_date_max

        if start_date != datetime.date(2006, 1, 1):
            start_date = (start_date + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
        else:
            start_date = start_date.strftime('%Y-%m-%d')
        end_date = datetime.date.today().strftime('%Y-%m-%d')
        
        insert_data_to_import_data_history(table_name, start_date, end_date)

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="password",
        database='stock_data'    
        )
        mycursor = mydb.cursor()
        sql = "SELECT code FROM stock_data.all_stock;"
        mycursor.execute(sql)
        for code in mycursor:
            process_data(code[0], start_date, end_date, adjust_flag, table_name)
        print(mycursor.rowcount, "was queried.") 
        mycursor.close()
        mydb.close()       

    bs.logout()

if __name__ == "__main__":
    main()


