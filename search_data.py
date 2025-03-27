def srch_data():
    try:
        import mysql.connector as m
        from tabulate import tabulate
        msc=m.connect(host='localhost',user='root',passwd='root',database='school')
        c=msc.cursor()
        print('1.Search by Name::')
        print('2.Seach by Roll no::')
        while True:
            ch=int(input('Enter choice::'))
            if ch==1:
                name1=input('Enter Name to be searched')
                c.execute("select * from student where name like %s", (f'%{name1}%',))
            elif ch ==2:
                rno1=input('Enter Roll Number of the student::')
                c.execute("select * from student where rno like %s", (rno1,))
            else:
                print('invalid input')
                return
            result=c.fetchall()
            if not result:
                print('No Data Found')
            else:
                headers = [i[0] for i in c.description]
                table = tabulate(result, headers, tablefmt="fancy_grid")
                print(table)
            x=input('Want to continue searching?(Y/N)')
            if x not in['Y','y']:
                break;
    except m.error as e:
        print('Error occured::{e}')
    finally:
        msc.commit()
        msc.close()











def srch_data1():
    try:
        import mysql.connector as m
        from tabulate import tabulate
        msc=m.connect(host='localhost',user='root',passwd='root',database='school')
        c=msc.cursor()
        print('1.Search by Emp no::')
        print('2.Seach by Name::')
        
        while True:
            ch=int(input('Enter choice::'))
            if ch==2:
                name1=input('Enter Name to be searched')
                c.execute("select * from staff where name like %s", (f'%{name1}%',))
            elif ch==1:
                rno1=input('Enter Emp Number of the Employee::')
                c.execute("select * from staff where name like %s", (rno1,))
            else:
                print('invalid input')
                return
            result=c.fetchall()
            if not result:
                print('No Data Found')
            else:
                headers = [i[0] for i in c.description]  # Get column names from the cursor
                table = tabulate(result, headers, tablefmt="fancy_grid")
                print(table)
            x=input('Want to continue searching?(Y/N)')
            if x not in['Y','y']:
                break;
    except m.error as e:
        print('Error occured::{e}')
    finally:
        msc.commit()
        msc.close()        

              
