from  tkinter import Frame
from  tkinter import Label
from  tkinter import font
from  tkinter import BOTH
from  tkinter import StringVar
from  tkinter import Button
from  tkinter import Tk
from  tkinter import messagebox
from  tkinter import ttk #theme
from  tkinter import Toplevel
from  tkinter import *
#from songline import Sendline
import csv
from datetime import datetime
#Import database
from db_Maintenance import *


#token ='x0wHaoiHWS1q2tlIYtMMffm5U8UtibhhrnYNt3c9eQi'
#messenger = Sendline(token)
GUI = Tk()
GUI.title('โปรแกรม')
GUI.geometry('1300x600+100+100')
####FONT#####
FONT1 = ('Angsana New' ,20,'bold')
FONT2 = ('Angsana New' ,15)
##################
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูข้อมูล')
Tab.add(T3,text='สรุป')
Tab.pack(fill=BOTH,expand=1)






####label####
L = Label (T1,text='ใบแจ้งซ่อม',font=FONT1)
L.place(x=80,y=10)

####
L = Label (T1,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name = StringVar()#ตัวแปรพิเศษ
E1 = ttk.Entry(T1,textvariable=v_name,font=FONT2)
E1.place(x=150,y=50)
#---------------
L = Label (T1,text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department = StringVar()
E2 = ttk.Entry(T1,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#---------------
L = Label (T1,text='อุปกรณ์',font = FONT2)
L.place(x=30,y=150)
v_machine = StringVar()
E3 = ttk.Entry(T1,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#---------------
L = Label (T1,text='อาการเสีย',font = FONT2)
L.place(x=30,y=200)
v_problem = StringVar()
E4 = ttk.Entry(T1,textvariable=v_problem,font=FONT2)
E4.place(x=150,y=200)
#---------------
L = Label (T1,text='หมายเลข',font = FONT2)
L.place(x=30,y=250)
v_number = StringVar()
E5 = ttk.Entry(T1,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#---------------
L = Label (T1,text='เบอร์ติดต่อ',font = FONT2)
L.place(x=30,y=300)
v_tel = StringVar()
E6 = ttk.Entry(T1,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)
#---------------

#def writecsv(record_list):
#    with open('data.csv','a',newline='',encoding='UTF-8') as file:
        #fw = csv.writer(file)
       # fw.writerow(record_list)

def save():
    name = v_name.get() # .get ดึงค่าออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง:'+ name + '\n'
    text = text +'แผนก:'+ department + '\n'
    text = text + 'อุปกรณ์:'+ machine + '\n'
    text = text + 'อาการเสีย:'+ problem + '\n'
    text = text + 'หมายเลข:'+ number + '\n'
    text = text + 'เบอร์โทร:'+ tel + '\n'
   
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tsid = str(int(datetime.now().strftime('%Y%m%H%M%S')) + 114152147165)
    #Gen Transactions
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)
    v_name.set('')
    v_department.set('')
    v_machine.set('')
    v_problem.set('')
    v_number.set('')
    v_tel.set('')
    update_table()
   # datalist =[dt,name,department,machine,problem,number,tel]
   # writecsv(datalist)
   # messenger.sendtext(text)
    messagebox.showinfo('กำลังบันทึก..',text)

#---------------
B = Button(T1, text='บันทึก',command=save)
B.place(x=150,y=350)
#---------------
#package ที่ใช้
# L.pack()
# L.grid(row=1,column=1)
# L.place(x=20,y=100)
# B.place
##############################tab2##################################
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทร']
headerw = [100,150,150,200,250,150,150]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=10)
mtworkorderlist.pack()

style = ttk.Style()
style.configure('Treeview.Heading',padding=(8,8),font=('Angsana New',20,'bold'))
style.configure('Treeview.Heading',rowheight=25,font=('AngsanaNew',15))

for h,w in zip(header,headerw):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w,anchor='w')
    
    
#mtworkorderlist.insert('','end',values=['A','B','C','D','E','H','G'])

data = view_mtworkorder()
#print(data)

def update_table():

    mtworkorderlist.delete(*mtworkorderlist.get_children())
    for d in data:
        d = list(d) #แปลง tuple เป็น list
        del d[0] # ลบ ID จาก DATABASE ออก
        mtworkorderlist.insert('','end',values=d)
       # mtworkorderlist.column('TSID',anchor='center')



def EditPage_mtworkorder(event=None):
    select = mtworkorderlist.selection()
    output = mtworkorderlist.item(select)
    print(output)
    
    GUI2 = Toplevel()
    GUI2.title('หน้าแก้ไขข้อมูล')
    GUI2.geometry('500x500')
    
    
    
    GUI2.mainloop() 

    
    
mtworkorderlist.bind('<Double-1>',EditPage_mtworkorder)




GUI.mainloop()

    
    




    
