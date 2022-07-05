#pip install mysql-connector-python
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv("host"),
  user=os.getenv("user"),
  password=os.getenv("password"),
  database=os.getenv("database"),
)
mycursor = mydb.cursor()
# create database
# mycursor.execute('create database student')
# mycursor.execute('show databases')

#create table

#Student table create
# mycursor.execute("drop table student")
mycursor.execute("CREATE TABLE student(id INT AUTO_INCREMENT PRIMARY KEY,first_name varchar(20),last_name varchar(20),middle_name varchar(20),feeid varchar(10),courseid varchar(10),contact_no INT)")
