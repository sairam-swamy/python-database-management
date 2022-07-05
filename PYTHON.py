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

    def delete(self):
        s_id = input('id of student to be deleted: ')
        self.mycursor.execute(f'Delete from student where id={s_id}')
        self.mydb.commit()
        print(f"student with id {s_id} deleted successfully!")

    def update(self):
        pass  

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
