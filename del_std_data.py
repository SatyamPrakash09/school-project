def del_data():
    try:
        import mysql.connector as m
        rno1=int(input('Enter Student Roll Number'))
        msc=m.connect(host='localhost',user='root',passwd='root',database='school')
        c=msc.cursor()
        s=("delete from student where rno= %s")
        c.execute(s,(rno1,))
        if c.rowcount==0:
            print('No Data Entered','\n','Empty Table')
            
        else:
            print('Data Deleted Successfully')
    
    except m.error as e:
        print('Check entered values','\n','error occured in del std module:::{e}')
    finally:
        msc.commit()
        msc.close()



        
def del_data1():
    try:
        import mysql.connector as m
        rno1=int(input('Enter Staff Emp Number'))
        msc=m.connect(host='localhost',user='root',passwd='root',database='school')
        c=msc.cursor()
        s=("delete from staff where rno= %s")
        c.execute(s,(rno1,))
        if c.rowcount==0:
            print('No Data Entered','\n','Empty Table')
            
        else:
            print('Data Deleted Successfully')
    
    except m.error as e:
        print('Check entered values','\n','error occured in del std module:::{e}')
    finally:
        msc.commit()
        msc.close()
