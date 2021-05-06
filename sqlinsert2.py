#!/usr/bin/python3
# Install python pip if you dont have. 
# sudo apt install python3-pip
# once pip is installed, install python-mysql connector
# pip3 install pymysql
# Note: apt is the repository for linux(ubuntu) apps, pip/pip3 is the repository for python apps.
# pymysql is a python library to execute SQL commands.

#Create a database using mysql cli
#login to mysql --> mysql -u <username> -p
#give your password
#once logged in create a new database --> CREATE DATABASE ab1;
#after this step, you can use python to execute data read and write to table

import pymysql

conn =pymysql.connect(database="users",user="admin",password="iotassignment3",host="localhost")
cur=conn.cursor()

#create database
#cur.execute("CREATE TABLE users(id int primary, name text, age int, gender text, address text);")

#to store user data

#uid = 3
name = input('Enter the name: ')
age = input('Enter the age: ')
city = input('Enter the city: ')
state= input('Enter the state: ')

data={'userName':name,'userAge':age, 'userCity':city,'userState':state}
print(data)

# Saving data to DB
cur.execute("INSERT INTO userdata (userName, userAge, userCity, UserState) VALUES (%(userName)s,%(userAge)s,%(userCity)s,%(userState)s);",data)
conn.commit()
print("saved to db")

#reading data from DB
#cur.execute("SELECT * FROM users;")
#get one row
#data1=cur.fetchone()
#get all rows
#data2=cur.fetchall()

#print(data1)
#print(data2)
