#basicsql.py
import sqlite3
'''
def save():
    name = v_name.get() # .get ดึงค่าออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()
'''

#connetion สร้าง conn เพื่อเชื่อมข้อมูล
conn = sqlite3.connect('maintenace.sqlite3')

#สร้าง cursor เป็นตัวที่เอาไว้สั่งคำสั่ง sql
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    name TEXT,
                    department TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    tel TEXT ) """)


def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    #create
    with conn: 
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit() #save database
#    print('saved')


def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
#    print(result)
    return result    


def update_mtworkorder(tsid,field,newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} =(?) WHERE tsid =(?)'.format(field)
        c.execute(command,(newvalue,tsid))       
    conn.commit()
 #   print('updated')




def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid =(?)'
        c.execute(command,([tsid]))
    conn.commit()
#    print('delete')
    

