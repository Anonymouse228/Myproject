import pymysql
import time
import os
import json

entr = 1
while entr:
    print('Enter MySQL data:', end='\n\n')
    host = input('hostname: ')
    name = input('username: ')
    password = input('password: ')
    print()
    try:
        entr = pymysql.connect(host, name, password)
        entr = 0
    except:
        print('Error!', end='\n\n')
        entr = 1


try:
    entr = pymysql.connect(host, name, password, 'project')
    with entr:
        entry = entr.cursor()
        entry.execute("drop table call1")
        entry.execute("create table call1(FromNum VARCHAR(255), ToNum VARCHAR(255), Start INT, Finish INT, Cost INT)")
except:
    entr = pymysql.connect(host, name, password)
    with entr:
        entry = entr.cursor()
        entry.execute("create database project")
        entry.execute("use project")
        entry.execute("create table tariff_plan(name VARCHAR(255), cost INT)")
        entry.execute("create table call1(FromNum VARCHAR(255), ToNum VARCHAR(255), Start INT, Finish INT, Cost INT)")
        entry.execute("insert into tariff_plan(name, cost) values('LTE', 10)")
        entry.execute("insert into tariff_plan(name, cost) values('CDMA', 15)")
        entry.execute("insert into tariff_plan(name, cost) values('GSM', 20)")
entry.execute("select * from tariff_plan")
rows = entry.fetchall()

a = 1
while True:
    try:
        r = open('Call' + str(a) + '.json', 'r')
        r = json.load(r)
        for row in rows:
            if row[0] == r['CallType']:
                CT = row[1]
        entr = pymysql.connect(host, name, password, 'project')
        with entr:
            entry = entr.cursor()
            entry.execute("insert into call1(FromNum, ToNum, Start, Finish, Cost) values(\'" + r['FromNum'] + "\', \'" + r['ToNum'] + "\', " + str(r['Start']) + ", " + str(r['Finish']) + ", " + str(round((r['Finish'] - r['Start']) / 60 * CT)) + ")")
        os.remove('Call' + str(a) + '.json')
        a += 1
    except:
        time.sleep(1)
