from DATABASE import get_mydb

## STUDENT CLASS

class Student:
    mydb = None
    mycursor = None
    def __init__(self) -> None:
        
        self.mydb = get_mydb()
        self.mycursor = self.mydb.cursor()

    def insert(self):
        first_name = input('Enter first name:')
        last_name = input('Enter lasy name:')
        middle_name = input('Enter middle name:')
        course_id = int(input('Enter course id:'))
        feeid = int(input('Enter fees ID:'))
        contact_no = input('Enter contact number:')
        self.mycursor.execute(f"INSERT INTO student(first_name, last_name, middle_name, feeid, courseid, contact_no) VALUES ('{first_name}','{last_name}', '{middle_name}','{feeid}','{course_id}', '{contact_no}');")
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")

    def delete(self):
        s_id = input('id of student to be deleted: ')
        self.mycursor.execute(f'Delete from student where id={s_id}')
        self.mydb.commit()
        print(f"student with id {s_id} deleted successfully!")

    def update(self):
        s_id = input('id of student: ')
        flag=True
        while(flag):
            print("1) Update contact number ,\n2) Update first_name ,\n3) Update last_name,\n4) Update middle_name,\n5) Update course_id, \n6) End Updating")
            ch = int(input("Enter choice:"))
            if(ch==1):
                contact_no = input('Enter the new contact number: ')
                self.mycursor.execute(f"UPDATE student SET contact_no = '{contact_no}' WHERE id= {s_id} ")
                self.mydb.commit()
            elif(ch==2):
                first_name = input('Enter the new first_name: ')
                self.mycursor.execute(f"UPDATE student SET first_name = '{first_name}' WHERE id= {s_id} ")
                self.mydb.commit()
            elif(ch==3):
                last_name = input('Enter the new last_name: ')
                self.mycursor.execute(f"UPDATE student SET last_name = '{last_name}' WHERE id= {s_id} ")
                self.mydb.commit()
            elif(ch==4):
                middle_name = input('Enter the new middle_name: ')
                self.mycursor.execute(f"UPDATE student SET middle_name = '{middle_name}' WHERE id= {s_id} ")
                self.mydb.commit()
            elif(ch==5):
                course_id = input('Enter the new course_id: ')
                self.mycursor.execute(f"UPDATE student SET course_id = '{course_id}' WHERE id= {s_id} ")
                self.mydb.commit()
            elif(ch==6):
                flag=False
                print("Thank You !")


    def search(self):
        id = int(input("Enter id of student: "))
        self.mycursor.execute(f" select * from student where id = {id}  ;")
        myresult = self.mycursor.fetchall()

        if len(myresult)==0:
            print('provide a valid ID')

        else:
            print(myresult)

    def display_all(self):
        
        self.mycursor.execute(f"select * from student ;")
        myresult = self.mycursor.fetchall()

        for data in myresult:
            print(data)
    
    def search_by_name(self):
        name = input("Enter first name of student: ")
        self.mycursor.execute(f"select * from student where first_name='{name}';")
        myresult = self.mycursor.fetchall()

        if len(myresult)==0:
            print('provide a valid name')

        else:
            print(myresult)

class Pay_roll:
    mydb = None
    mycursor = None
    def __init__(self) -> None:
        
        self.mydb = get_mydb()
        self.mycursor = self.mydb.cursor()

    # ADD new pay_roll
    def insert(self):
        pay_roll_id = input('Enter pay_roll_id:')
        staff_id = input('Enter staff_id:')
        basic_salary = input('Enter basic_salary:')

        self.mycursor.execute(f"INSERT INTO pay_roll (pay_roll_id, staff_id, basic_salary) VALUES ('{pay_roll_id}','{staff_id}', '{basic_salary}');")
        self.mydb.commit()
        
        print(self.mycursor.rowcount, "record inserted.")

    # display pay_roll 
    def display_all(self):
        self.mycursor.execute(f" select * from pay_roll;")
        myresult = self.mycursor.fetchall()
        for data in myresult:
            print(data)
    
    # Search Function  
    def search(self, id):
        self.mycursor.execute(f" select * from pay_roll where pay_roll_id = {id}  ;")
        myresult = self.mycursor.fetchall()
        if len(myresult)==0:
            print('provide a valid ID')
        else:
            print(myresult)
 

    # Delete Function                
    def delete(self, id):
        self.mycursor.execute(f" DELETE from pay_roll where pay_roll_id = { id } ;")
        print(self.mycursor.rowcount, "record(s) deleted")


    # Update Function
    def update_salary(self, id, basic_salary):
        self.mycursor.execute(f"UPDATE pay_roll SET basic_salary = '{basic_salary}' WHERE pay_roll_id= {id} ")
        print(self.mycursor.rowcount, "record(s) updated")
        

## PAYROLL CLASS

class PayRollGrp2:

  def insert(self):
    pay_id = input('Enter pay roll name:')
    staff_id = input('Enter staff Id:')
    basic = input('Enter basic salary:')
    gross = input('Enter gross salary:')
    pf = input('Enter pf amount:')
    allowence = input('Enter allowence amount:')
    extra = input('Enter extras amount:')
    total = input('Enter total package amount:')

    mycursor.execute(f"INSERT INTO pay_role_details VALUES ('{pay_id}','{staff_id}', '{basic}','{gross}','{pf}', '{allowence}','{extra}','{total}');")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  # display student 
  def display(self):
    mycursor.execute(f"select * from pay_role_details ;")
    myresult = mycursor.fetchall()
    for data in myresult:
      print(data)
    
  # Search Function  
  def search(self, id):
    mycursor.execute(f" select * from pay_role_details where pay_roll_id = {id}  ;")
    myresult = mycursor.fetchall()
    if len(myresult)==0:
      print('provide a valid ID')
    else:
      print(myresult)
 

  # Delete Function                
  def delete(self, id):
    mycursor.execute(f" DELETE from pay_role_details where pay_roll_id = { id } ;")

    print(mycursor.rowcount, "record(s) deleted")


  # Update Function
  def update(self, id, basic,gross,pf,allowence,extra,total):
    mycursor.execute(f"UPDATE pay_role_details SET basic_salary = '{basic}',gross_salary='{gross}',pf_amount='{pf}',allowence='{allowence},extra='{extra},total_amount='{total}' WHERE pay_roll_id= {id}; ")

    print(mycursor.rowcount, "record(s) updated")
    
  
## SUBJECT CLASS

class Subject:

  # insert subject names and id for a given course
  def insert(self):
    subject_id = input('Enter Subject ID : ')
    name = input('Enter name of Subject : ')
    course_id = input('Enter Course ID fot the student')

    mycursor.execute(f"INSERT INTO subjects (subject_id, name, course_id) VALUES ('{subject_id}','{name}', '{course_id}');")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  # display subjects in a given course 
  def display(self):
    mycursor.execute(f" select * from subjects ;")
    myresult = mycursor.fetchall()
    for data in myresult:
      print(data)
    
  # Search a subject  

  def search(self, id):
    mycursor.execute(f" select * from subjects where subject_id = {id}  ;")
    myresult = mycursor.fetchall()
    if len(myresult)==0:
      print('provide a valid ID')
    else:
      print(myresult)
 

  # Delete a subject                
  def delete(self, id):
    mycursor.execute(f" DELETE from subjects where subject_id = { id } ;")
    print(mycursor.rowcount, "record(s) deleted")

  # Update a subject
  def update(self, id, name):
    mycursor.execute(f"UPDATE subjects SET name = '{name}' WHERE id= {id} ")

    print(mycursor.rowcount, "record(s) updated")
    
    
## ROUTINE CLASS

class Routine:

  # ADD new routine record
  def insert(self):
    routine_id = int(input('Enter Routine name:'))
    course_id = int(input("Enter the Course ID:") )
    subject_id = int(input("Enter the subject ID:")) 
    staff_id = int(input("Enter the staff ID:") )
    start_time = input("Enter the starting time of the routine:") 
    day_name = input("Enter the day at which routine is done :") 
    end_time = input("Enter the ending time of the routine:") 
    mycursor.execute(f"insert into routine (routine_id,course_id,subject_id,staff_id,start_time,day_name,end_time) VALUES ('{routine_id}','{course_id}','{subject_id}','{staff_id}','{start_time}','{day_name}','{end_time}');")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  # display routine record
  def display(self):
    mycursor.execute(f" select * from routine ;")
    res = mycursor.fetchall()
    for i in res:
      print(i)
    
  # Search Function  
  def search(self, id):
    mycursor.execute(f" select * from routine where routine_id = {id}  ;")
    res = mycursor.fetchall()
    if len(res)==0:
      print('provide a valid ID')
    else:
      print(res)
 

  # Delete Function                
  def delete(self, id):
    mycursor.execute(f" delete from routine where routine_id = { id } ;")

    print(mycursor.rowcount, "record(s) deleted")


  # Update Function
  def update(self, id,staff_id):
    mycursor.execute(f"update routine set  staff_id= '{staff_id}' where routine_id= {id} ; ")
    
    
    print(mycursor.rowcount, "record(s) updated")
    
    
## FEE PACKAGE CLASS
 
class fee_packages:
    mydb = None
    mycursor = None
    def __init__(self) -> None:
        
        self.mydb = get_mydb()
        self.mycursor = self.mydb.cursor()

    def insert(self):
        fee_id = input('Enter Fees Id:')
        name = input('Enter name of this fee package:')

        amount = input('Enter amount for this fee package:')
        self.mycursor.execute(f"INSERT INTO fee_packages (fee_id, name, amount) VALUES ('{fee_id}','{name}', '{amount}');")
        self.mydb.commit()
        print(self.mycursor.rowcount, "record inserted.")

    # display package 
    def display(self):
        self.mycursor.execute(f" select * from fee_packages ;")
        myresult = self.mycursor.fetchall()
        for data in myresult:
            print(data)
    
    # Search Package 
    def search(self, id):
        self.mycursor.execute(f" select * from fee_packages where fee_id = {id}  ;")
        myresult = self.mycursor.fetchall()
        if len(myresult)==0:
            print('provide a valid ID')
        else:
            print(myresult)
 

    # Delete Package                
    def delete(self, id):
        self.mycursor.execute(f" DELETE from fee_packages where fee_id = { id } ;")

        print(self.mycursor.rowcount, "record(s) deleted")
        
## STAFF CLASS
    
class staff:
    def headtail(self,value):
        print("========== "+value+" ==========")
        
    def staffMain(self):
#         mydb = mysql.connector.connect(  #local connectivity creadentials
#                 host="localhost",
#                 user="root",
#                 password="1234",
#                 database="school"
#         )
#         myc = mydb.cursor()

        userid = 1002  # user_id will be directly iniate here after successfull user login
        while True:
            flag=True
            choice=int(input("1.View Profile\n2.Update\n3.Request to PayRoll Sheet\n4.Exit\n"))
            print("You choose: "+str(choice)+"\n")
            
            if choice==1:   #read
                myc.execute("select first_name, middle_name, last_name, payroll_id, contact_no from staff where userid="+str(userid)+"")
                res = myc.fetchall()
                headtail("Personal Details")
                for x in res:
                    print("First Name: "+x[0])
                    print("Middle Name: "+x[1])
                    print("Last Name: "+x[2])
                    print("Contact No: "+str(x[4]))
                    print("Payroll Id: "+str(x[3]))
                headtail("XXXX")

            elif choice==2: #update
                headtail("Update Details")
                ch=int(input("1.Change first_name\n2.Change middle_name\n3.Change last_name\n4.Change contact no\n5.None\n"))
                print("You choose: "+str(ch)+"\n")
                val = ""
                if ch!=5:
                    val = input("Enter here: ")
                sub = ""

                if ch==1:
                    sub = "first_name='"+val+"'"
                elif ch==2:
                    sub = "middle_name='"+val+"'"
                elif ch==3:
                    sub = "last_name='"+val+"'"
                elif ch==4:
                    sub = "contact_no="+val+""
                elif ch==5:
                    flag=False
                    headtail("OOPS! SOMETHING WENT WRONG")
                    headtail("XXXX")
                else:
                    flag=False
                    print("Invalid Choice!!")
                    headtail("XXXX")
                    
                if flag:
                    sql = "UPDATE staff SET "+str(sub)+" WHERE userid="+str(userid)+""
                    myc.execute(sql)
                    mydb.commit()
                    headtail("Data Updated Successfully!")
                    headtail("XXXX")
                    
            elif choice==3:  #subquery read operation
                headtail("REQ PROCESSING....")
                # Subquery for data retrieval
                sql = "select id,userid,basic_sal,gross_sal,pf_amount,allowence,total_pay from pr where id in (select payroll_id from staff where userid="+str(userid)+")"
                myc.execute(sql)
                res = myc.fetchall()
                headtail("PayRoll Sheet")
                for x in res:
                    print("Payroll Id: "+str(x[0]))
                    print("User Id: "+str(x[1]))
                    print("Basic Salary: "+str(x[2]))
                    print("Gross Salary: "+str(x[3]))
                    print("PF amount: "+str(x[4]))
                    print("Total Pay: "+str(x[6]))
                headtail("XXXX")
                
            elif choice==4: #exit code
                ex = input("Are you sure? y/n: ")
                if ex == "y" or ex=="yes":
                    print("bye bye :)")
                    break
            else:
                print("Invalid Choice!!")
                
                
## USER CLASS

class User:
    

    def insert(self):
        user_id = int(input('Enter User ID:'))
        email = input('Enter Email ID:')
        user_pass = input('Enter Password:')
        time=input('Enter timestamp:')
        role_id=int(input('Enter role id:'))
        
        mycursor.execute(f"INSERT INTO user1(user_id, email, user_pass, time, role_id) VALUES ('{user_id}','{email}', '{user_pass}','{time}','{role_id}');")
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    def delete(self):
        user_id = input('id of user to be deleted: ')
        mycursor.execute(f'Delete from user1 where user_id={user_id}')
        mydb.commit()
        print(f"user with id {user_id} deleted successfully!")

    def update(self):
        user_id = input('id of user: ')
        flag=True
        while(flag):
            print("1) Update email  ,\n2) Update password")
            ch = int(input("Enter choice:"))
            if(ch==1):
                email = input('Enter the new email: ')
                mycursor.execute(f"UPDATE user1 SET email = '{email}' WHERE user_id= {user_id} ")
                mydb.commit()
            elif(ch==2):
                user_pass = input('Enter the new password: ')
                mycursor.execute(f"UPDATE user1 SET password = '{user_pass}' WHERE user_id= {user_id} ")
                mydb.commit()
            


    def search(self):
        user_id = int(input("Enter id of user: "))
        mycursor.execute(f" select * from user1 where user_id = {user_id}  ;")
        myresult =mycursor.fetchall()

        if len(myresult)==0:
            print('provide a valid ID')

        else:
            print(myresult)

    def display_all(self):
        
        mycursor.execute(f"select * from user1;")
        myresult = mycursor.fetchall()

        for data in myresult:
            print(data)

    obj=User()

    flag=True
    try:
        while(flag):
            print("1) Insert  ,\n2) Delete, \n3) Update, \n4) Search, \n5)Display")
            ch = int(input("Enter choice:"))
            if(ch==1):
                obj.insert()
            elif(ch==2):
               obj.delete()
            elif(ch==3):
               obj.update()
            elif(ch==4):
            	obj.search()
            elif(ch==5):
            	obj.display_all()
            else:
            	flag=False
            	print("Thank You!")
    except:
    	print("Print valid data")

                
                
## COURSES CLASS
                
class Courses:

    # insert course id and name
    def insert(self):
        course_id = input('Enter Course ID : ')
        name = input('Enter Name of the Course : ')
        mycursor.execute(f"INSERT INTO courses (course_id, name) VALUES ('{course_id}','{name}');")
        mydb.commit()
        print(mycursor.rowcount, "Record(s) inserted.")

    # display all courses
    def display(self):
        mycursor.execute(f" select * from courses ;")
        myresult = mycursor.fetchall()
        for data in myresult:
            print(data)

    # Search for a course
    def search(self, id):
        mycursor.execute(f" select * from courses where course_id = {id}  ;")
        myresult = mycursor.fetchall()
        if len(myresult) == 0:
            print('Provide a Valid Course ID!')
        else:
            print(myresult)

    # Delete a course
    def delete(self, id):
        mycursor.execute(f" DELETE from courses where course_id = {id} ;")
        print(mycursor.rowcount, "Record(s) deleted")

    # Update a course
    def update(self, id, name):
        mycursor.execute(f"UPDATE courses SET name = '{name}' WHERE course_id= {id} ")

        print(mycursor.rowcount, "Record(s) updated")
