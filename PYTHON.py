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
        s_id = input('id of student: ')
        contact_no = input('Enter the new contact number: ')
        self.mycursor.execute(f"UPDATE student SET contact_no = '{contact_no}' WHERE id= {s_id} ")
        self.mydb.commit()


    def search(self):
        pass

    def display(self, ob):
        pass
