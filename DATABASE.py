#pip install mysql-connector-python
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

def get_mydb():  
    
    mydb = mysql.connector.connect(
    host=os.getenv("host"),
    user=os.getenv("user"),
    password=os.getenv("password"),
    database=os.getenv("database"),
    )
    return mydb



# create database
# mycursor.execute('create database student')
# mycursor.execute('show databases')

def create_table():
    
    mydb = get_mydb()
    mycursor = mydb.cursor()
    #create table

    #Student table create
    #TODO update query with foreign keys when user, course, fee table are created
    mycursor.execute("drop table student")
    mydb.commit()
    mycursor.execute("CREATE TABLE student(id INT AUTO_INCREMENT PRIMARY KEY,userid varchar(10), first_name varchar(20),last_name varchar(20),middle_name varchar(20),feeid varchar(10),courseid varchar(10),contact_no varchar(20))")
    mydb.commit()

    # note - create role table before user table
    # mycursor.execute('CREATE TABLE `user`(user_id int auto_increment primary key, username varchar(16) not null, email varchar(255) not null, `password` varchar(32) not null, create_time timestamp not null DEFAULT CURRENT_TIMESTAMP, role_id int not null, foreign key (role_id) references `role`(role_id));')

def create_pay_roll_table():
    
    mydb = get_mydb()
    mycursor = mydb.cursor()
    #create table

    #Pay roll table create
    #TODO update query with foreign keys
    mycursor.execute("drop table pay_roll")
    mydb.commit()

    # Table for reference
    # create table pay_roll (
    #     pay_roll_id int primary key,
    #     staff_id int,
    #     basic_salary int not null,
    #     -- gross_salary int,
    #     -- pf_amount int,
    #     -- allowance int,
    #     -- extras int,
    #     -- total_pay int
    # );
    mycursor.execute("CREATE TABLE pay_roll(pay_roll_id int primary key, staff_id int, basic_salary int not null);")
    mydb.commit()
