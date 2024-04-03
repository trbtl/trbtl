
import sqlite3
import datetime
import pandas as pd

x = datetime.datetime.now()
date_stamp = str(x)
satisfaction = "9"
comment = "Because the primary key consists of one column, you"

conn = sqlite3.connect('utils.db')
c = conn.cursor()
# Create the database and table 
sql1 = '''CREATE TABLE IF NOT EXISTS survey ("stamp" TEXT, "rating" TEXT, "comments" TEXT)'''
print(sql1)
c.execute(sql1)
conn.commit()

sqls = """SELECT name FROM sqlite_master"""
c.execute(sqls)

tables = c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
for table_name in tables:
    table_name = table_name[0] # tables is a list of single item tuples
    table = pd.read_sql_query("SELECT * from {} LIMIT 0".format(table_name), conn)
    print(table_name)
    for col in table.columns:
        print('\t' + col)
    # print()
print(c.fetchall())


sql2 = f'''INSERT INTO survey (date_stamp, rating, comments) VALUES ('{date_stamp}', '{satisfaction}', '{comment}')'''
print(sql2)
c.execute(sql2)
conn.commit()

c.execute('''SELECT * FROM survey''')
rows = c.fetchall()
for row in rows:
    print(row)

#  UNIQUE NOT NULL,


conn.close()

def save_data(date_stamp, satisfaction, comment):
    print(date_stamp + " - " + satisfaction + " - " + comment)
    # try:
    conn = sqlite3.connect('utils.db')
    c = conn.cursor()
    # Insert the data
    # sql = '''INSERT INTO survey (date_stamp, rating, comments) VALUES (date_stamp, satisfaction, comment)'''
    sql = f'''INSERT INTO survey (date_stamp, rating, comment) VALUES ('{date_stamp}', '{satisfaction}', '{comment}')'''
    print(sql)
    c.execute(sql)
    conn.commit()
    conn.close()
        # return 1
    # except:
    #     return 0
    
def show_data():
    print("Results:")
    conn = sqlite3.connect('utils.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM survey''')
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

# x = datetime.datetime.now()
# date_stamp = str(x)
# satisfaction = "9"
# comment = "Because the primary key consists of one column, you can use the column constraint."

# success = save_data(date_stamp, satisfaction, comment)
# print(success)
# show_data()