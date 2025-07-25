import mysql.connector as m
from inserting_values import *
from del_std_data import *
from show_data import *
from search_data import *

msc=m.connect(host='localhost',user='root',passwd='root')
myc=msc.cursor()
myc.execute('show databases')
myc.fetchall()
myc.execute("create database if not exists School")
myc.execute("use School")
myc.execute("create table if not exists student(rno int(10) not null,name varchar(50) not null,class int(4),gender char(1),primary key(rno))")
myc.execute("create table if not exists staff(emp_no int(10) not null,name varchar(50) not null,gender char(1),salary varchar(25),primary key(emp_no))")
msc.commit()
print('''
________________________________________________________________________________
                        SCHOOL DATABASE MANAGEMENT SYSTEM
________________________________________________________________________________
''')
try:
    while True:
        print('0.Show tables')
        print('1.Enter data for new student::')
        print('2.Delete data of student::')
        print('3.Enter data for new staff::')
        print('4.Delete data of staff::')
        print('5.Search Student::')
        print('6.Search Staff::')
        print('7.Exit')
        ch = int(input('Enter your choice::'))
        # Entering new data:
        if ch == 0:
            print('All information prompted are mandatory to be filled', '\n', 'Add Student Data')
            result = show_data()
            print(result)

        elif ch == 1:
            print('All information prompted are mandatory to be filled', '\n', 'Add Student Data')
            result1 = add_data()
            print(result1)
        elif ch == 2:
            print('All information prompted are mandatory to be filled', '\n', 'Delete Student Data')
            result2 = del_data()
            print(result2)
        elif ch == 3:
            print('All information prompted are mandatory to be filled', '\n', 'Add Staff Data')
            result3 = add_data1()
            print(result3)
        elif ch == 4:
            print('All information prompted are mandatory to be filled', '\n', 'Delete Staff Data')
            result4 = del_data1()
            print(result4)

        elif ch == 5:
            print('All information prompted are mandatory to be filled', '\n', 'Search Student Data')
            result5 = srch_data()
            print(result5)

        elif ch == 6:
            print('All information prompted are mandatory to be filled', '\n', 'Search Staff Data')
            result6 = srch_data1()
            print(result6)

        elif ch == 7:
            print('''EXIT
                                    --------------By Satyam Prakash''')
            break
        print("Want to Continue(Main Menu)?(Y/N)")
        ch1 = input('Enter the Choice')
        if ch1 not in ['Y', 'y']:
            print('''Program exited.
                                    -------------By Satyam Prakash''')
            break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    msc.close()
    
        

            
