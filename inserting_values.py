def add_data():
    try:
        import mysql.connector as m
        msc=m.connect(host='localhost',user='root',passwd='root',database='school')
        m=msc.cursor()
        while True:
            a=int(input('Enter roll_no of the student::'))
            b=input('Enter Name of the student::')
            c=int(input('Enter class of the student::'))
            d=input('Enter Gender of the Student::')
            o="insert into student values({},'{}',{},'{}')".format(a,b,c,d)
            m.execute(o)
            r=m.rowcount
            print("Data Added")
            if r==0:
                print("Duplicate data")
            else:
                print("Data inserted")
            x=input("want to continue inserting data?")
            if x not in ['y','Y']:
                break;
    except m.Error as e:
        return f"Error adding data to the database:{e}"
    except AttributeError:
        print('error occured')
    finally:
        msc.commit()
        m.close()
        msc.close()

            







def add_data1():
    try:
        
        import mysql.connector as m
        msc=m.connect(host='localhost',user='root',passwd='root',database='school')
        m=msc.cursor()
        while True:
            a=int(input('Enter Emp Number of Employee::'))
            b=input('Enter Name of the Employee::')
            c=input('Enter gender(M/F/O)::')
            d=int(input('Enter Salary of Employee::'))
            o="insert into staff values({},'{}','{}',{})".format(a,b,c,d)
            m.execute(o)
            msc.commit()
            r=m.rowcount
            print("Data Added")
            if r==0:
                print("Duplicate data")
            else:
                print("Data inserted")
            x=input("want to continue inserting data?")
            if x not in ['y', 'yes','Y']:
                break;
    except m.error as e:
        return f"Error adding data to the database:{e}"
    except AttributeError:
        print('error occured')
    finally:
        m.close()
        msc.close()
        
        

