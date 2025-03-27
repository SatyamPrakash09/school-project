import mysql.connector as c
from tabulate import tabulate
def show_data():
    try:
        msc=c.connect(host='localhost',user='root',passwd='root',database='school')
        m=msc.cursor()
        print('1.Show Student data')
        print('2.Show Staff data')
        ch=int(input('Enter your choice'))
        if ch == 1:
            m.execute("select * from student")
            data = m.fetchall()
            if not data:
                print('No data present')
            else:
                headers = [i[0] for i in m.description]
                table = tabulate(data,headers,tablefmt="fancy_grid")
                print(table)
        elif ch == 2:
            m.execute('select * from staff')
            data1 = m.fetchall()
            if not data1:
                print('No data present')
            else:
                headers = [i[0] for i in m.description]
                table = tabulate(data1, headers, tablefmt="fancy_grid")
                print(table)
        else:
            print('inavalid choice')
            
    except m.error as e:
        print('An error occured in show data module::{e}')
