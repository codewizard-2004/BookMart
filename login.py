from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import dataloader
import time

root=ttk.Window(themename='solar')
root.geometry('1000x569+500+180')
root.resizable(0,0)
root.title('BookMart.in')

main_bg=PhotoImage(file='assets/background/Picture1.png')
eye_img=PhotoImage(file='assets/buttons/eye1.png')
main_label=Label(root,image=main_bg)
main_label.pack()

flag=2
def changeimg():
    global flag
    if flag==1:
        textL.config(image=text_img1)
        flag+=1
    elif flag==2:
        textL.config(image=text_img2)
        flag+=1
    elif flag==3:
        textL.config(image=text_img3)
        flag=1
    root.update_idletasks()
    textL.after(5000,changeimg)

text_img1=PhotoImage(file='assets/background/text1.png')
text_img2=PhotoImage(file='assets/background/text2.png')
text_img3=PhotoImage(file='assets/background/text3.png')


textL=Label(root,image=text_img1,width=385,height=86)
textL.place(x=10,y=470)
textL.after(5000,changeimg)


#===============================LOGIN============================================
count=0
def after_login():
    def changemeter():
        global count
        if count==0:
            meter.configure(subtext='Updating Offers')
            meter.configure(amountused=20)
            count+=1
            meter.after(3000,changemeter)
        elif count==1:
            meter.configure(subtext='Opening Books')
            meter.configure(amountused=50)
            count+=1
            meter.after(3000,changemeter)
        elif count==2:
            meter.configure(subtext='Refreshing Cataouge')
            meter.configure(amountused=90)
            count+=1
            meter.after(2000,changemeter)
        elif count==3:
            meter.configure(subtext='Almost There!!!')
            meter.configure(amountused=99)
            count+=1
            meter.after(2000,root.destroy)
    main_label.pack_forget()
    textL.place_forget()
    usernameL.place_forget()
    passwordL.place_forget()
    forgetp.place_forget()
    eyeL.place_forget()
    logB.place_forget()
    mail.place_forget()
    name.place_forget()
    usernameS.place_forget()
    passwordS.place_forget()
    eyeS.place_forget()
    dt.place_forget()
    terms.place_forget()
    pc.place_forget()
    signB.place_forget()
    meter=ttk.Meter(root,bootstyle='primary',subtext='Connecting to server',textright='%')
    meter.pack(pady=150)
    meter.after(1000,changemeter)
    
def after_login():
    root.destroy()
    dataloader.open_main()

def login():
    u=usernameL.get()
    p=passwordL.get()
    if  dataloader.try_login(u,p)==1:
        Messagebox.show_info('Welcome Back','Login')
        after_login()
    elif u=='' or p=='':
        Messagebox.show_warning('Please Enter all credentials','Forgot Password')
    else:
        Messagebox.show_warning('Incorrect Username or Password','Login')

def forgotpass(e):
    u=usernameL.get()
    if u=='':
        Messagebox.show_warning('Please Enter username','Forgot Password')
    elif dataloader.check_user(u)!=1:
        Messagebox.show_warning('This account does not exist','Login')
    else:
        r=ttk.Window(themename='solar')
        r.geometry('400x300+500+180')
        r.resizable(0,0)
        r.title('Account Recovery')
        Label(r,text='We will send the \npassword to your \nregistered E-Mail address',bg='dark blue',
                  font=('Helvatica',16)).pack()
        Label(r,text='\n').pack()
        Label(r,text='Username: '+u,bg='dark blue',font=('Helvatica',16)).pack()
        data=dataloader.get_data(u)
        Label(r,text='E-Mail: '+data[0],bg='dark blue',font=('Helvatica',16)).pack()
        def sender():
            Messagebox.show_info('Please check your E-Mail','Account Recovery')
            r.destroy()
        sent=Button(r,text='Send',width=30,bg='blue',command=sender)
        sent.pack()
        

e1=0
def openeye(e):
    global e1
    if e1==0:
        g=passwordL.get()
        passwordL.delete(0,END)
        passwordL.config(show='')
        passwordL.insert(0,g)
        e1=1
    else:
        g=passwordL.get()
        passwordL.delete(0,END)
        passwordL.config(show='*')
        passwordL.insert(0,g)
        e1=0

usernameL=ttk.Entry(root,bootstyle='primary',width=30,font=('Helvatica',10))
usernameL.place(x=600,y=90)

passwordL=ttk.Entry(root,bootstyle='primary',width=30,font=('Helvatica',10),show='*')
passwordL.place(x=600,y=130)

forgetp=ttk.Label(root,text='forgot password?',font=('Helvatica 7 underline'),bootstyle='primary')
forgetp.place(x=660,y=165)
forgetp.bind('<Button-1>',forgotpass)

eyeL=Label(root,image=eye_img,height=22,width=33)
eyeL.place(x=890,y=130)
eyeL.bind('<Button-1>',openeye)

logB=ttk.Button(root,text='Log-In',bootstyle='primary',width=10,command=login)
logB.place(x=600,y=450)

#===============================SIGNIN===========================================

def signin():
    email=mail.get()
    nam=name.get()
    username=usernameS.get()
    date=dt.entry.get()    
    password=passwordS.get()
    a=dataloader.check_user(username,email)
    if email=='' or nam=='' or username=='' or date=='' or password=='':
        Messagebox.show_warning('Please Enter all credentials','Sign-In')
        return
    elif a==1:
        Messagebox.show_info('An account with this\nusername or E-Mail already exists','Sign-In')
        mail.delete(0,END)
        usernameS.delete(0,END)
    else:
        dataloader.add_user(email,nam,username,date,password)
        mail.delete(0,END)
        name.delete(0,END)
        usernameS.delete(0,END)
        passwordS.delete(0,END)
    


def termsf(e):
    r=ttk.Window(themename='solar')
    r.geometry('500x500+500+180')
    r.resizable(0,0)
    r.title('Terms and Privacy Policy')

e2=0
def openeyeS(e):
    global e2
    if e2==0:
        g=passwordS.get()
        passwordS.delete(0,END)
        passwordS.config(show='')
        passwordS.insert(0,g)
        e2=1
    else:
        g=passwordS.get()
        passwordS.delete(0,END)
        passwordS.config(show='*')
        passwordS.insert(0,g)
        e2=0

mail=ttk.Entry(root,bootstyle='primary',width=30,font=('Helvatica',10))
mail.place(x=600,y=250)

name=ttk.Entry(root,bootstyle='primary',width=30,font=('Helvatica',10))
name.place(x=600,y=290)

usernameS=ttk.Entry(root,bootstyle='primary',width=30,font=('Helvatica',10))
usernameS.place(x=600,y=330)

passwordS=ttk.Entry(root,bootstyle='primary',width=30,font=('Helvatica',10),show='*')
passwordS.place(x=600,y=402)

eyeS=Label(root,image=eye_img,height=22,width=33)
eyeS.place(x=890,y=402)
eyeS.bind('<Button-1>',openeyeS)

dt=ttk.DateEntry(root,bootstyle='primary',width=34)
dt.place(x=600,y=365)
dt.entry.delete(0,END)

terms=ttk.Label(root,text='terms',font=('Helvatica 7 underline'))
terms.place(x=683,y=533)
terms.bind('<Button-1>',termsf)

pc=ttk.Label(root,text='privacy policy',font=('Helvatica 7 underline'))
pc.place(x=745,y=533)
pc.bind('<Button-1>',termsf)

signB=ttk.Button(root,text='Sign-In',bootstyle='info',width=10,command=signin)
signB.place(x=750,y=450)


root.mainloop()
