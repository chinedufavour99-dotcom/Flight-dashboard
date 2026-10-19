from tkinter import *
from PIL import Image,ImageTk #PIL is used to import your image into tkinter
import sqlite3 
import subprocess
from tkinter import ttk
from tkinter import messagebox as msg

usersRole = ["admin","user","other"]

top = Tk()
top.geometry("500x400+300+0")
top.title("Signup Page")
top.config(background="White")
top.resizable(0,0)
image = Image.open("bg.jpg")
photo = ImageTk.PhotoImage(image)

def signup():
    subprocess.Popen(["python","signin.py"])


def sign():
    fullname = ent1.get()
    username = ent2.get()
    userrole = ent3.get()
    password = ent4.get()
    remark = txt1.get("1.0","end")
    if username=="" or password=="" or remark=="":
        msg.showinfo("Alert","Empty record is not allowed, please fill the form")
    else:
            con = sqlite3.connect('airline.db')
            cur = con.cursor()
    try:
            cur.execute('''INSERT INTO users(fullname,username,userrole,password,remark) 
                            VALUES(?,?,?,?,?)''',(fullname,username,userrole,password,remark)) #the blue values represent anything that is connected to the database
            # for record to show in the table of database you comit
            con.commit()
            msg.showinfo("Alert","Successfully registered")
            top.destroy()
            signup()

    except:
        msg.showinfo("Alert","Record Already Exists")

ImageLabel = Label(top,image=photo)
ImageLabel.place(relheight=1,relwidth=1)

lbl1=Label(top,text="SignUp Page", font=("verdana",20,"bold"), foreground="#000000", background="White", underline=5)
lbl1.grid(row=0, column=1)

lbl2=Label(top,text="Full Name:", font=("verdana",10,"bold"), foreground="#000000", background="White", underline=5)
lbl2.grid(row=1,column=0, pady=10)
ent1=Entry(top,width=50, relief=FLAT) #relief changes the visual of your box from 3D to 2D
ent1.grid(row=1,column=1)

lbl3=Label(top,text="USERNAME:", font=("verdana",10,"bold"), foreground="#000000", background="White", underline=5)
lbl3.grid(row=2,column=0, pady=10)
ent2=Entry(top,width=50, relief=FLAT)
ent2.grid(row=2,column=1)

lbl4=Label(top,text="User Role:", font=("verdana",10,"bold"), foreground="#000000", background="white", underline=5)
lbl4.grid(row=3,column=0, pady=10)
ent3=ttk.Combobox(width=40, value=usersRole)
ent3.grid(row=3,column=1)

lbl5=Label(top,text="PASSWORD:", font=("verdana",10,"bold"), foreground="#000000", background="White", underline=5)
lbl5.grid(row=4,column=0)
ent4=Entry(top,width=50, relief=FLAT, show="*")
ent4.grid(row=4,column=1, pady=10)

lbl6=Label(top,text="REMARK:", font=("verdana",10,"bold"), foreground="#000000", background="White", underline=5)
lbl6.grid(row=5,column=0)
txt1=Text(top,width=40,height=10)
txt1.grid(row=5,column=1, pady=10)

btn=Button(top, text="Sign Up", foreground="black", background="white", width=20, command=sign)
btn.grid(row=6,column=1)

top.mainloop()