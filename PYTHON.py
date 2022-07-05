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
