from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.scrolled import ScrolledText
#from ttk.bootstrap.tableview import Tableview
import dataloader
import time
import random


root=ttk.Window(themename='superhero')
root.geometry('1900x1000+0+0')
root.resizable(0,0)
root.title('BookMart.in')

#===================cart
cart=[]
price=0
price2=0
#=====================================top frame(menu,search)===================================
cord=-200
press=False
def move():
    global cord
    global press
    if press==False:
        if cord==20:
            press=True
            return
        else:
            side_frame.place(x=cord,y=100)
            cord+=20
            side_frame.after(1,move)
    if press==True:
        if cord==-220:
            press=False
            return
        else:
            side_frame.place(x=cord,y=100)
            cord-=20
            side_frame.after(1,move)
            
black=ttk.Style(theme='superhero')
black.theme_use('superhero')
black.configure('Custom.TFrame',background='black')

black2=ttk.Style(theme='superhero')
black2.theme_use('superhero')
black2.configure('Custom.TLabel',background='black',foreground='gold')

top_frame=ttk.Frame(root,width=2000,height=100,style='Custom.TFrame')
top_frame.pack()

menu_img=PhotoImage(file='assets/buttons/menu.png')
main_logo=PhotoImage(file='assets/buttons/logo.png')
acc_logo=PhotoImage(file='assets/buttons/acc.png')
acoin=PhotoImage(file='assets/background/coin1.png')

Label(top_frame,image=main_logo,width=280).place(x=100,y=-5)

sf_flag=0
sb_click=0
def chtext(e):
    global sb_click
    if sb_click==0:
        search_bar.delete(0,END)
        searchframe.place(x=500,y=70)
        sb_click=1
        return
    else:
        search_bar.insert(0,'Search by Book,author or genre.....')
        searchframe.place_forget()
        sb_click=0
        return
    
def retext(e):
    typed=search_bar.get()
    data=dataloader.get_book_data(title='no')
    if typed=='':
        for i in data:
            searchlb.insert(END,'                            '+i[1])
    else:
        D=[]
        for i in data:
            if typed.lower() in i[1].lower():
                D.append('                            '+i[1])
                searchlb.delete(0,END)
        for i in D:
            searchlb.insert(END,i)

def sbuy(e):
    sel=searchlb.get(ANCHOR)
    data=dataloader.get_book_data(title='no')
    for i in data:
        if i[1]==sel.strip():
            buy_window(i)

search_bar=ttk.Entry(top_frame,width=50,font=('Helvatica ',16),bootstyle='danger')
search_bar.place(x=500,y=20)
search_bar.insert(0,'Search by Book,author or genre.....')
search_bar.bind('<Button-1>',chtext)
search_bar.bind('<KeyRelease>',retext)

side_button=Button(top_frame,command=move,image=menu_img,width=50)
side_button.place(x=10,y=20)


click_acc_flag=0
def click_acc(e):
    global click_acc_flag
    if click_acc_flag==0:
        workframe.place(x=1300,y=100)
        ttk.Label(workframe,text='Hello,User',font=('Helvatica 15 underline'),style='Custom.TLabel').place(x=100,y=10)
        ttk.Label(workframe,text='Signed In as: amalv2004',font=('Helvatica 15'),style='Custom.TLabel').place(x=0,y=50)
        ttk.Label(workframe,text='Type:             Regular',font=('Helvatica 15'),style='Custom.TLabel').place(x=0,y=100)
        ttk.Button(workframe,text='Update Address',width=30,bootstyle='info').place(x=20,y=200)
        ttk.Button(workframe,text='Upgrade to Crown',width=30,bootstyle='danger').place(x=20,y=250)
        click_acc_flag=1
        return
    if click_acc_flag==1:
        workframe.place_forget()
        click_acc_flag=0
        return



acc_but=Label(top_frame,image=acc_logo,width=50,height=47)
acc_but.place(x=1400,y=25)
acc_but.bind('<Button-1>',click_acc)



ttk.Label(top_frame,text='|Trending this week|',font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=500,y=70)
ttk.Label(top_frame,text='Special Offers|',font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=646,y=70)
ttk.Label(top_frame,text='All Time Best|',font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=755,y=70)
ttk.Label(top_frame,text='Romantic|',font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=856,y=70)
ttk.Label(top_frame,text="Children's Book|",font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=930,y=70)
ttk.Label(top_frame,text='Redeem Code|',font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=1050,y=70)
ttk.Label(top_frame,text='Get Discounts|',font=('Helvatica 10 underline'),style='Custom.TLabel').place(x=1159,y=70)

#=======================================ad_frame=========================================
ad_frame=ttk.Frame(root,width=1700,height=200,bootstyle='info')
ad_frame.pack()
    

ad_flag=0
def change_ad_r():
    if ad_label1.winfo_x()==10200:
        ad_label1.place(x=-1700,y=0)
    if ad_label2.winfo_x()==10200:
        ad_label2.place(x=-1700,y=0)
    if ad_label3.winfo_x()==10200:
        ad_label3.place(x=-1700,y=0)
    if ad_label4.winfo_x()==10200:
        ad_label4.place(x=-1700,y=0)
    if ad_label5.winfo_x()==10200:
        ad_label5.place(x=-1700,y=0)
    if ad_label6.winfo_x()==10200:
        ad_label6.place(x=-1700,y=0)
    if ad_label7.winfo_x()==10200:
        ad_label7.place(x=-1700,y=0)
    global ad_flag
    if ad_flag==170:
        ad_flag=0
        ad_frame.after(60000,change_ad_r)
        return
    else:
        ad_label1.place(x=ad_label1.winfo_x()+10,y=0)
        ad_label7.place(x=ad_label7.winfo_x()+10,y=0)
        ad_label6.place(x=ad_label6.winfo_x()+10,y=0)
        ad_label5.place(x=ad_label5.winfo_x()+10,y=0)
        ad_label4.place(x=ad_label4.winfo_x()+10,y=0)
        ad_label3.place(x=ad_label3.winfo_x()+10,y=0)
        ad_label2.place(x=ad_label2.winfo_x()+10,y=0)

        ad_label1.after(1,change_ad_r)
        ad_flag+=1
        root.update_idletasks()
    

ad_img1=PhotoImage(file='assets/background/ad1.png')
ad_img2=PhotoImage(file='assets/background/ad2.png')
ad_img3=PhotoImage(file='assets/background/ad3.png')
ad_img4=PhotoImage(file='assets/background/ad4.png')
ad_img5=PhotoImage(file='assets/background/ad5.png')
ad_img6=PhotoImage(file='assets/background/ad6.png')
ad_img7=PhotoImage(file='assets/background/ad7.png')

ad_label2=Label(ad_frame,image=ad_img4)
ad_label3=Label(ad_frame,image=ad_img3)
ad_label4=Label(ad_frame,image=ad_img2)
ad_label1=Label(ad_frame,image=ad_img1)
ad_label5=Label(ad_frame,image=ad_img5)
ad_label6=Label(ad_frame,image=ad_img6)
ad_label7=Label(ad_frame,image=ad_img7)

ad_label1.place(x=0,y=0)
ad_label2.place(x=-1700,y=0)
ad_label3.place(x=-3400,y=0)
ad_label4.place(x=-5100,y=0)
ad_label5.place(x=-6800,y=0)
ad_label6.place(x=-8500,y=0)
ad_label7.place(x=-10200,y=0)

ad_frame.after(60000,change_ad_r)

#============================content frame======================================================================
def buy_window(e):
    def add_to_cart(k):
        global cart,price
        if k in cart:
            Messagebox.show_warning('Item already added','Buy')
            r.destroy()
        else:
            cart.append(k)
            Messagebox.show_info('Added to cart','Buy')
            tree.insert('','end',value=(str(len(cart)),k[1],k[4]))
            price+=float(k[4])
            r.destroy()
    r=ttk.Toplevel()
    r.geometry('800x700+600+200')
    r.resizable(0,0)
    r.title('BookMart.in')
    global kkk
    kkk=PhotoImage(file='assets/data/books/cover/'+e[6])
    ttk.Label(r,image=kkk).place(x=10,y=50)
    Label(r,text='Title: '+e[1],font=('Helvatica 15'),bg='blue').place(x=200,y=50)
    Label(r,text='Author: '+e[2],font=('Helvatica 15'),bg='blue').place(x=200,y=100)
    Label(r,text='Type: '+e[3],font=('Helvatica 15'),bg='blue').place(x=200,y=150)
    Label(r,text='About This Book:',font=('Helvatica 10'),bg='blue').place(x=200,y=280)
    st=Text(r,height=10,width=95,font=('Helvatica 9'))
    st.place(x=0,y=300)
    desc=dataloader.get_book_desc(int(e[0]),'f')
    st.insert(END,desc)
    st.config(state='disabled')
    Label(r,text='Price: '+e[4]+'Rs or ',font=('Helvatica 15'),bg='blue').place(x=0,y=520)
    Label(r,text=str(dataloader.ac(float(e[4]))),font=('Helvatica 15'),bg='blue').place(x=250,y=520)
    Label(r,image=acoin).place(x=310,y=520)
    atc=ttk.Button(r,text='Add to Cart',width=25,bootstyle='info',command=lambda:add_to_cart(e))
    atc.place(x=0,y=560)
    rte=ttk.Button(r,text='Rate  ',width=25,bootstyle='info')
    rte.place(x=0,y=650)
        
def fill_refu():
    books=dataloader.get_book_data('no')
    b1=random.choice(books)
    books.remove(b1)
    b2=random.choice(books)
    books.remove(b2)
    b3=random.choice(books)
    books.remove(b3)

    global img_refu1
    img_refu1=PhotoImage(file='assets/data/books/cover/'+b1[6])
    global img_refu2
    img_refu2=PhotoImage(file='assets/data/books/cover/'+b2[6])
    global img_refu3
    img_refu3=PhotoImage(file='assets/data/books/cover/'+b3[6])
   
    xcords=[225,830,1370]
    ximage=[50,650,1190]
    ycords=[50,100,150,200,250,300,350]
    images=[img_refu1,img_refu2,img_refu3]
    Title=[b1[1],b2[1],b3[1]]
    author=[b1[2],b2[2],b3[2]]
    release=[b1[7],b2[7],b3[7]]
    rating=[b1[8],b2[8],b3[8]]
    sale=[b1[5],b2[5],b3[5]]

    for i in range(3):
        Label(refu,image=images[i]).place(x=ximage[i],y=50)
        ttk.Label(refu,text=Title[i],font=('Helvatica 15 underline'),bootstyle='inverse-light').place(x=xcords[i],y=50)
        ttk.Label(refu,text='--By '+author[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=100)
        ttk.Label(refu,text='Released: '+release[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=150)
        ttk.Label(refu,text='Rating: '+rating[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=200)
        ttk.Label(refu,text='Copies sold: '+sale[i],font=('Helvatica 15'),bootstyle='inverse-light').place(x=xcords[i],y=250)
    butt1=ttk.Button(refu,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b1)).place(x=225,y=350)
    butt2=ttk.Button(refu,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b2)).place(x=830,y=350)
    butt3=ttk.Button(refu,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b3)).place(x=1370,y=350)

def fill_bestseller():        
    x=dataloader.find_bestseller()
    b1=x[0]
    b2=x[1]
    b3=x[2]
    global img_bs1
    img_bs1=PhotoImage(file='assets/data/books/cover/'+b1[6])
    global img_bs2
    img_bs2=PhotoImage(file='assets/data/books/cover/'+b2[6])
    global img_bs3
    img_bs3=PhotoImage(file='assets/data/books/cover/'+b3[6])
   
    xcords=[225,830,1370]
    ximage=[50,650,1190]
    ycords=[50,100,150,200,250,300,350]
    images=[img_bs1,img_bs2,img_bs3]
    Title=[b1[1],b2[1],b3[1]]
    author=[b1[2],b2[2],b3[2]]
    release=[b1[7],b2[7],b3[7]]
    rating=[b1[8],b2[8],b3[8]]
    sale=[b1[5],b2[5],b3[5]]
    for i in range(3):
        Label(bestseller,image=images[i]).place(x=ximage[i],y=50)
        ttk.Label(bestseller,text=Title[i],font=('Helvatica 15 underline'),bootstyle='inverse-light').place(x=xcords[i],y=50)
        ttk.Label(bestseller,text='--By '+author[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=100)
        ttk.Label(bestseller,text='Released: '+release[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=150)
        ttk.Label(bestseller,text='Rating: '+rating[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=200)
        ttk.Label(bestseller,text='Copies sold: '+sale[i],font=('Helvatica 15'),bootstyle='inverse-light').place(x=xcords[i],y=250)
    butt1=ttk.Button(bestseller,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b1)).place(x=225,y=350)
    butt2=ttk.Button(bestseller,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b2)).place(x=830,y=350)
    butt3=ttk.Button(bestseller,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b3)).place(x=1370,y=350)

def fill_trending():
    x=dataloader.find_trending()
    b1=x[0]
    b2=x[1]
    b3=x[2]
    global img_t1
    img_t1=PhotoImage(file='assets/data/books/cover/'+b1[6])
    global img_t2
    img_t2=PhotoImage(file='assets/data/books/cover/'+b2[6])
    global img_t3
    img_t3=PhotoImage(file='assets/data/books/cover/'+b3[6])
   
    xcords=[225,830,1370]
    ximage=[50,650,1190]
    ycords=[50,100,150,200,250,300,350]
    images=[img_t1,img_t2,img_t3]
    Title=[b1[1],b2[1],b3[1]]
    author=[b1[2],b2[2],b3[2]]
    release=[b1[7],b2[7],b3[7]]
    rating=[b1[8],b2[8],b3[8]]
    sale=[b1[5],b2[5],b3[5]]
    for i in range(3):
        Label(topg,image=images[i]).place(x=ximage[i],y=50)
        ttk.Label(topg,text=Title[i],font=('Helvatica 15 underline'),bootstyle='inverse-light').place(x=xcords[i],y=50)
        ttk.Label(topg,text='--By '+author[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=100)
        ttk.Label(topg,text='Released: '+release[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=150)
        ttk.Label(topg,text='Rating: '+rating[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=200)
        ttk.Label(topg,text='Copies sold: '+sale[i],font=('Helvatica 15'),bootstyle='inverse-light').place(x=xcords[i],y=250)
    butt1=ttk.Button(topg,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b1)).place(x=225,y=350)
    butt2=ttk.Button(topg,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b2)).place(x=830,y=350)
    butt3=ttk.Button(topg,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b3)).place(x=1370,y=350)

def fill_newest():
    x=dataloader.find_newest()
    b1=x[0]
    b2=x[1]
    b3=x[2]
    global img_n1
    img_n1=PhotoImage(file='assets/data/books/cover/'+b1[6])
    global img_n2
    img_n2=PhotoImage(file='assets/data/books/cover/'+b2[6])
    global img_n3
    img_n3=PhotoImage(file='assets/data/books/cover/'+b3[6])
   
    xcords=[225,830,1370]
    ximage=[50,650,1190]
    ycords=[50,100,150,200,250,300,350]
    images=[img_n1,img_n2,img_n3]
    Title=[b1[1],b2[1],b3[1]]
    author=[b1[2],b2[2],b3[2]]
    release=[b1[7],b2[7],b3[7]]
    rating=[b1[8],b2[8],b3[8]]
    sale=[b1[5],b2[5],b3[5]]
    for i in range(3):
        Label(newbook,image=images[i]).place(x=ximage[i],y=50)
        ttk.Label(newbook,text=Title[i],font=('Helvatica 15 underline'),bootstyle='inverse-light').place(x=xcords[i],y=50)
        ttk.Label(newbook,text='--By '+author[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=100)
        ttk.Label(newbook,text='Released: '+release[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=150)
        ttk.Label(newbook,text='Rating: '+rating[i],font=('Helvatica',15),bootstyle='inverse-light').place(x=xcords[i],y=200)
        ttk.Label(newbook,text='Copies sold: '+sale[i],font=('Helvatica 15'),bootstyle='inverse-light').place(x=xcords[i],y=250)
    butt1=ttk.Button(newbook,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b1)).place(x=225,y=350)
    butt2=ttk.Button(newbook,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b2)).place(x=830,y=350)
    butt3=ttk.Button(newbook,text='View Item',bootstyle='danger',width=25,command=lambda:buy_window(b3)).place(x=1370,y=350)

my_canvas=ttk.Canvas(root,scrollregion=(0,0,2000,2500))
my_canvas.pack(fill=BOTH,expand=True,side=LEFT)

refu=ttk.Frame(my_canvas,width=1690,height=500,bootstyle='light')
topg=ttk.Frame(my_canvas,width=1690,height=500,bootstyle='light')
bestseller=ttk.Frame(my_canvas,width=1690,height=500,bootstyle='light')
newbook=ttk.Frame(my_canvas,width=1690,height=500,bootstyle='light')

ttk.Label(refu,text='Recomended for you',font=('Helvatica',16),bootstyle='inverse-light').place(x=0,y=0)
ttk.Label(topg,text='Trending',font=('Helvatica',16),bootstyle='inverse-light').place(x=0,y=0)
ttk.Label(bestseller,text='Best Sellers',font=('Helvatica',16),bootstyle='inverse-light').place(x=0,y=0)
ttk.Label(newbook,text='Newest Release',font=('Helvatica',16),bootstyle='inverse-light').place(x=0,y=0)

my_canvas.create_window(955,300,window=refu)
my_canvas.create_window(955,900,window=topg)
my_canvas.create_window(955,1500,window=bestseller)
my_canvas.create_window(955,2100,window=newbook)

#to fix mouse wheel
my_canvas.bind('<MouseWheel>',lambda event: my_canvas.yview_scroll(-int(event.delta/60),'units'))

scrollbar=ttk.Scrollbar(root,orient='vertical',command=my_canvas.yview,bootstyle='light-round')
my_canvas.configure(yscrollcommand=scrollbar.set)
scrollbar.place(x=1900,y=0,relheight=1,anchor='ne')

fill_refu()
fill_bestseller()
fill_trending()
fill_newest()
#=====================================================setting side frame================================================
side_frame=ttk.Frame(root,width=200,height=990,style='Custom.TFrame')
side_frame.place(x=-200,y=100)

cart_frame=Frame(root,width=700,height=700,bg='dark blue')

#----------------------------------TreeView in wallet--------------------------------------------------------
def remove_item():
    try:
        selected=tree.selection()[0]
        item=tree.focus()
        rem_item=tree.item(item)
        tree.delete(selected)
        global cart ,price
        for i in cart:
            if i[1]==rem_item['values'][1]:
                cart.remove(i)
        price=0
        for i in cart:
            price+=float(i[4])
        price_label.configure(text='Total Price: '+str(price)[0:8]+ 'Rs  or')
        price_label2.configure(text=str(dataloader.ac(price)))
    except:
        Messagebox.show_warning('No items selected','Remove from cart')

column=('#1','#2','#3')
tree=ttk.Treeview(cart_frame,bootstyle='success',columns=column,show='headings',height=15)
tree.column('#1',anchor=CENTER,stretch=NO,width=200)
tree.heading('#1',text='SerialNo')
tree.column('#2',anchor=CENTER,stretch=NO,width=300)
tree.heading('#2',text='Items')
tree.column('#3',anchor=CENTER,stretch=NO,width=200)
tree.heading('#3',text='Price(Rs)')

treescroll=ttk.Scrollbar(cart_frame,orient='vertical',command=tree.yview,bootstyle='success-round')
tree.configure(yscrollcommand=treescroll.set)

price_label=ttk.Label(cart_frame,text='',font=('Helvatica 16'),bootstyle='primary')
price_label2=ttk.Label(cart_frame,text=str(dataloader.ac(price)),font=('Helvatica 15'),bootstyle='primary')

def cart_confirm(e):
    global cart , price
    def down_pdf():
        pass
    rec=ttk.Toplevel()
    rec.geometry('950x700+600+200')
    rec.resizable(0,0)
    rec.title('BookMart.in')
    if e=='cod':
        ttk.Label(rec,text='Purchace Recipt',font=('Helvatica 20 underline'),bootstyle='primary').place(x=300,y=0)
        ttk.Label(rec,text='Date:',font=('Helvatica 16'),bootstyle='primary').place(x=10,y=50)
        ttk.Label(rec,text='You have Purchased the following',font=('Helvatica 16'),bootstyle='primary').place(x=200,y=150)
        Y=200
        for i in cart:
            ttk.Label(rec,text='⭐'+i[1]+' by '+i[2]+'\t'+'Price: '+i[4],font=('Helvatica 10'),bootstyle='primary').place(x=200,y=Y)
            Y+=50
        ttk.Label(rec,text='Total Price: '+str(price),font=('Helvatica 16'),bootstyle='primary').place(x=10,y=500)
        ttk.Label(rec,text='Your items will be delivered to your registered address within five days\n you must show the recipt during delivery. For any details please contact us',
              font=('Helvatica 16'),bootstyle='primary').place(x=10,y=550)
        dow=ttk.Button(rec,text='Download Recipt',bootstyle='primary',width=19,command=down_pdf)
        dow.place(x=10,y=650)
        
    if e=='ac':
        ttk.Label(rec,text='Purchace Recipt',font=('Helvatica 20 underline'),bootstyle='primary').place(x=300,y=0)
        ttk.Label(rec,text='Date:',font=('Helvatica 16'),bootstyle='primary').place(x=10,y=50)
        ttk.Label(rec,text='You have Purchased the following',font=('Helvatica 16'),bootstyle='primary').place(x=200,y=150)
        Y=200
        for i in cart:
            ttk.Label(rec,text='⭐'+i[1]+' by '+i[2]+'\t'+'Price: '+i[4],font=('Helvatica 10'),bootstyle='primary').place(x=200,y=Y)
            Y+=50
        ttk.Label(rec,text='Your items will be delivered to your registered address within five days\n for any details please contact us',
              font=('Helvatica 16'),bootstyle='primary').place(x=10,y=550)
        dow=ttk.Button(rec,text='Download Recipt',bootstyle='primary',width=19,command=down_pdf)
        dow.place(x=10,y=650)
    

def exit_window():
    if Messagebox.okcancel('Do you want to sign-out and exit','Exit'):
        root.destroy()

def home_press():
    my_canvas.pack(fill=BOTH,expand=True,side=LEFT)
    cart_frame.place_forget()
def cart_press():
    if cart==[]:
        Messagebox.show_warning('Cart is empty','Cart')
        home_press()
        return
    my_canvas.pack_forget()
    cart_frame.place(x=600,y=350)
    ttk.Label(cart_frame,text='name       :Amal Varghese',font=('Helvatica 16'),bootstyle='primary').place(x=0,y=0)
    ttk.Label(cart_frame,text='Username: amalv2004',font=('Helvatica 16'),bootstyle='primary').place(x=0,y=30)
    tree.place(x=0,y=70,relwidth=1)
    treescroll.place(x=685,y=70,relheight=0.48)
    ttk.Button(cart_frame,text='Remove Selected Item',bootstyle='danger',command=remove_item).place(x=0,y=410)
    conf=ttk.Button(cart_frame,text='Confirm',bootstyle='primary',width=19,command=lambda:cart_confirm('cod'))
    conf.place(x=0,y=550)
    price_label.configure(text='Total Price: '+str(price)[0:8]+ 'Rs  or')
    price_label2.configure(text=str(dataloader.ac(price)))
    price_label.place(x=0,y=450)
    price_label2.place(x=350,y=450)
    ttk.Label(cart_frame,image=acoin).place(x=450,y=450)



ttk.Label(side_frame,text='Welcome,User',font=('Helvatica 16 underline'),style='Custom.TLabel').place(x=7,y=200)

cart_img=PhotoImage(file='assets/buttons/cart.png')
wallet_img=PhotoImage(file='assets/buttons/wallet.png')
contact_img=PhotoImage(file='assets/buttons/contact.png')
exit_img=PhotoImage(file='assets/buttons/exit.png')

home_b=Button(side_frame,text='HOME',width=23,height=3,command=home_press)
home_b.place(x=5,y=300)
cart_b=Button(side_frame,image=cart_img,height=58,width=190,command=cart_press)
cart_b.place(x=5,y=500)
exit_b=Button(side_frame,image=exit_img,height=54,width=190,command=exit_window).place(x=5,y=700)

workframe=ttk.Frame(root,width=300,height=300,style='Custom.TFrame')
searchframe=ScrolledFrame(root,width=765,height=300,autohide=True,style='light')
searchlb=Listbox(searchframe,width=765,height=300,font=('Helvatica 15'))
searchlb.bind('<<ListboxSelect>>',sbuy)
searchlb.pack()

root.mainloop()
