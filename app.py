from tkinter import *
import smtplib

i=0

def s_mail():
    global a


def log():
    global a
    global i
    if i==1:    
        a=Label(text="Login successfull")
        a.place(x=30,y=230)
        button = Button(app,text="send mail",command=s_mail,width="15",height="1",bg="grey")
        button.place(x=30,y=250)

    else:
        a=Label(text="Login error")
        a.place(x=30,y=230)

def login():
    email=mail.get()
    password=pas.get()
    global i
    i=1
    log()

app=Tk()
app.geometry("500x500")
app.title("Login")
heading=Label(text="Login")
heading.pack()

log_mail = Label(text="Email:")
passwd = Label(text="password:")
 
log_mail.place(x=30,y=20)
passwd.place(x=30,y=90)
 
mail = StringVar()
pas = StringVar()
 
login_mail = Entry(textvariable=mail,width="30")
pass_entry = Entry(textvariable=pas,width="30")
 
login_mail.place(x=30,y=50)
pass_entry.place(x=30,y=130)

button = Button(app,text="login",command=login,width="15",height="1",bg="grey")
button.place(x=30,y=170)
print(i)

mainloop()