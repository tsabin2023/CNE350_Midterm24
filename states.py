# Tyler Sabin
# CNE350 Midterm Spring Quarter 2024
# 5/10/2024
# forked from https://github.com/ellisju37073/States and modified by Tyler Sabin

import pandas
from sqlalchemy import create_engine

hostname="127.0.0.1"
uname="root"
pwd=""
dbname="zipcodes"

engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
            .format(host=hostname, db=dbname, user=uname, pw=pwd))

tables = pandas.read_csv(r"Populationstate.csv")



connection=engine.connect()
tables.to_sql('states',con = engine, if_exists = 'replace')
connection.close()
print(tables)