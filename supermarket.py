from tkinter import *
import sqlite3 as db

con = db.connect("C://Users//RHiNO//Desktop//foroshgah//kala.db")
c = con.cursor()
c.execute("create table if not exists kala(name text primary key,gheymat_kharid integer,gheymat_forosh integer,tedad integer)")
con.commit()


def add():
    v1 = x1.get()
    v2 = x2.get()
    v3 = x3.get()
    v4 = x4.get()
    c.execute("insert into kala values('{}',{},{},{})".format(v1, v2, v3, v4))
    con.commit()
    show()


def search():
    lsb.delete(0, END)
    c.execute("select * from kala where name='{}'".format(x1.get()))
    info = c.fetchall()
    for i in info:
        lsb.insert(END, i)

def delete():
    c.execute("delete from kala where name='{}'".format(x1.get()))
    con.commit()
    show()

def edit():
    v1 = x1.get()
    v2 = x2.get()
    v3 = x3.get()
    v4 = x4.get()

    c.execute("update kala set gheymat_kharid={},gheymat_forosh={},tedad={} where name='{}'".format(v2, v3, v4, v1))
    con.commit()
    show()

def show():
    lsb.delete(0, END)
    c.execute("select * from kala")
    info = c.fetchall()
    for i in info:
        lsb.insert(END, i)

def close():
    w.destroy()

def zarb():
    lsb.delete(0, END)  
    v2 = x2.get()   
    v4 = x4.get()   
    result = v2 * v4
    x3.set(result)
    lsb.delete(0, END)




w = Tk()
w.title("مدیریت کالا")
w.geometry("600x350")

l1 = Label(w,text="نام کالا",width = 10)
l1.place(x=20,y=20)

l2 = Label(w,text="قیمت خرید",width = 10)
l2.place(x=300,y=20)

l3 = Label(w,text="قیمت فروش",width = 10)
l3.place(x=20,y=60)

l4 = Label(w,text="تعداد",width = 10)
l4.place(x=300,y=60)

x1 = StringVar()
e1 = Entry(w,textvariable=x1,width=20)
e1.place(x=90,y=20)

x2 = IntVar()
e2 = Entry(w,textvariable=x2,width=20)
e2.place(x=370,y=20)

x3 = IntVar()
e3 = Entry(w,textvariable=x3,width=20,state="disabled")
e3.place(x=90,y=60)

x4 = IntVar()
e4 = Entry(w,textvariable=x4,width=20)
e4.place(x=370,y=60)

lsb = Listbox(w, width=55, height=10)
lsb.place(x=20, y=100)

scroll = Scrollbar(w)
scroll.place(x=390, y=130, height=80)
lsb.config(yscrollcommand=scroll.set)
scroll.config(command=lsb.yview)

b1 = Button(w,text="اضافه کردن",width=15,command = add)
b1.place(x=480,y=100)

b2 = Button(w,text="جستجوی کالا",width=15,command = search)
b2.place(x=480,y=130)

b3 = Button(w,text="حذف کالا",width=15,command=delete)
b3.place(x=480,y=160)

b4 = Button(w,text="ویرایش",width=15,command=edit)
b4.place(x=480,y=190)

b5 = Button(w,text="بستن",width=15,command=close)
b5.place(x=480,y=220)

b6 = Button(w,text="ضرب",width=15,command = zarb)
b6.place(x=480,y=250)

w.mainloop()
