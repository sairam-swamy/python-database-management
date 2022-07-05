from DATABASE import get_mydb

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
    
    
class fees:

  # insert package
  def insert(self):
    fee_id = input('Enter Fee ID : ')
    name = input('Enter name of course : ')
    amount = input('Enter amount of the course')

    mycursor.execute(f"INSERT INTO fees (fee_id, name, amount) VALUES ('{fee_id}','{name}', '{amount}');")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  # display package 
  def display(self):
    mycursor.execute(f" select * from fees;")
    myresult = mycursor.fetchall()
    for data in myresult:
      print(data)
    
  # Search a package  
  def search(self, fee_id):
    mycursor.execute(f" select * from fees where fee_id = {fee_id}  ;")
    myresult = mycursor.fetchall()
    if len(myresult)==0:
      print('provide a valid ID')
    else:
      print(myresult)
 

  # Delete a package                
  def delete(self, fee_id):
    mycursor.execute(f" DELETE from fees where fee_id = { fee_id } ;")
    print(mycursor.rowcount, "record(s) deleted")

  # Update a course name
  def update(self, fee_id, name):
    mycursor.execute(f"UPDATE fees SET name = '{name}' WHERE id= {fee_id} ")

    print(mycursor.rowcount, "record(s) updated")

class subjects:
    def insert(self):
        sub_id=input("Enter subject id")
        sub_name=input("Enter subject name")
        course_id=input("Enter course id")
        mycursor.execute(f"insert into subjects(sub_id,name,course_id) values('{sub_id}','{sub_name}','{course_id}');")
        mydb.commit()
        print(mycursor.rowcount,"row inserted")

    def display(self):
        mycursor.execute(f" select * from subjects ;")
        result = mycursor.fetchall()
        for data in result:
            print(data)

    def search(self, sub_id):
        mycursor.execute(f" select * from subjects where sub_id = {sub_id}  ;")
        result = mycursor.fetchall()
        if len(result) == 0:
            print('provide a valid subject ID')
        else:
            print(result)

    def delete(self, sub_id):
        mycursor.execute(f" DELETE from subjects where sub_id = {sub_id} ;")

        print(mycursor.rowcount, "record(s) deleted")

    def update(self, sub_id, name):
        mycursor.execute(f"UPDATE subjects SET name = '{name}' WHERE sub_id= {sub_id} ")

        print(mycursor.rowcount, "records updated")
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
    

class fee_packages:


  # ADD new fee package
  def insert(self):
    fee_id = input('Enter Fees Id:')
    name = input('Enter name of this fee package:')

    amount = input('Enter amount for this fee package:')
    mycursor.execute(f"INSERT INTO fee_packages (fee_id, name, amount) VALUES ('{fee_id}','{name}','{amount}');")
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

  # display package 
  def display(self):
    mycursor.execute(f" select * from fee_packages ;")
    myresult = mycursor.fetchall()
    for data in myresult:
      print(data)
    
  # Search Package 
  def search(self, id):
    mycursor.execute(f" select * from fee_packages where fee_id = {id}  ;")
    myresult = mycursor.fetchall()
    if len(myresult)==0:
      print('provide a valid ID')
    else:
      print(myresult)
 

  # Delete Package                
  def delete(self, id):
    mycursor.execute(f" DELETE from fee_packages where fee_id = { id } ;")
    mydb.commit()
    print(mycursor.rowcount, "record(s) deleted")

    
    
# an object of fee_packages class
obj = fee_packages()
flag =True
try:
    while flag:
        #check whether user is staff or student 
        print("Enter staff/student/close")
        userid = input("Enter your user id:")

        #if user is staff or ( if  userid in staff table )
        if (userid=='staff'):
            print("1) Enter new package,\n2) List all packages ,\n3) find package,\n4) delete fee package")

            ch = int(input("Enter choice:"))
            if(ch == 1):
                obj.insert()
                    
            elif(ch == 2):
                print("\n")
                print("\nList of packages\n")  
                obj.display()
                        
            elif(ch == 3):
                obj.search(int(input('Enter fee ID no:')))
                # obj.display(list1[s])
                        
            elif(ch == 4):
                obj.delete(int(input('Enter fee ID no:')))

                        
            else:
                flag=False
                print("Thank You !")

        #if user is student or (userid in student table )
        elif (userid =='student'):

            s_id = input('Enter your fee ID:')
            

            mycursor.execute(f" select * from fee_packages where fee_id = {s_id}  ;")
            myresult = mycursor.fetchall()
            if len(myresult)==0:
                print('No DATA Found')
            else:
                print('Here are your fee details:')
                print(myresult) 
        elif (userid == "close"):
            flag=False

        #if user is neither staff nor student
        else:
            print('Please enter valid user id!')

except:
    print('provide a valid data')         
