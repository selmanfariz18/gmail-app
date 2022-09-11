from tkinter import *
import smtplib

i=0

def send_message(email_body,address):
    global a
    address_info = address
    
    email_body_info = email_body
    
    server.sendmail(email,address_info,email_body_info)
    
    print("Message sent")

def s_mail():
    global a

    address_field = Label(text="Recipient Address :")
    email_body_field = Label(text="Message :")

    address_field.place(x=15,y=290)
    email_body_field.place(x=15,y=360)

    address = StringVar()
    email_body = StringVar()


    address_entry = Entry(textvariable=address,width="30")
    email_body_entry = Entry(textvariable=email_body,width="30")

    address_entry.place(x=15,y=320)
    email_body_entry.place(x=15,y=400)

    button = Button(app,text="Send Message",command=lambda: send_message(email_body.get(),address.get()),width="15",height="1",bg="grey")

    button.place(x=15,y=440)

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
    global server
    global email
    email=mail.get()
    password=pas.get()
    global i
    sender_email = email 
    
    sender_password = password
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    
    server.starttls()
    
    server.login(sender_email,sender_password)
    
    print("Login successful")
    i=1
    log()

app=Tk()
app.geometry("500x500")
app.title("Login")
heading=Label(text="Gmail App")
heading.pack()

log_mail = Label(text="Email:")
passwd = Label(text="password:\n(Use app password generated from google security)")

 
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


d=Label(text="Developed by selmanul farizy")
d.place(x=40,y=480)

mainloop()