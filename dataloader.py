import csv
import os
import random

db='assets/data/user.csv'

#[Email,Name,Username,DOB,Password]
#[sno,title,author,genre,price,sale,pic,date,rate]

def check_user(username,Email=''):
    '''Checks weather an account exists with given username or email
returns 1 if yes'''
    file=open(db)
    data= csv.reader(file)
    try:
        for i in data:
            if i[2]==username or i[0]==Email:
                return 1
    except:
        pass

def find_bestseller():
    '''returns the serial no of the most sold books in a list in ascending order'''
    x=get_book_data('no')
    x1={}
    for i in x:
        x1[int(i[0])]=int(i[5])
    val=list(x1.values())
    val.sort(reverse=True)
    keys=[]
    for i in val:
        for j in x1:
            if x1[j]==i:
                keys.append(j)
    final=[]
    for i in keys:
        for j in x:
            if int(j[0])==i:
                final.append(j)
    return final

def find_trending():
    '''reurns the list of books in the asending order of trending books'''
    x=get_book_data('no')
    x1={}
    for i in x:
        x1[int(i[0])]=float(i[8])
    val=list(x1.values())
    val.sort(reverse=True)
    keys=[]
    for i in val:
        for j in x1:
            if x1[j]==i:
                keys.append(j)
    final=[]
    for i in keys:
        for j in x:
            if int(j[0])==i:
                final.append(j)
    return final

def find_newest():
    '''returns the list of books sorted by date'''
    x=get_book_data('no')
    x1={}
    for i in x:
        x1[int(i[0])]=float(i[7])
    val=list(x1.values())
    val.sort(reverse=True)
    keys=[]
    for i in val:
        for j in x1:
            if x1[j]==i:
                keys.append(j)
    final=[]
    for i in keys:
        for j in x:
            if int(j[0])==i:
                if j in final:
                    pass
                else:
                    final.append(j)
    return final


def get_book_data(title):
    '''returns all book entries if title==no then titles will be removed'''
    file=open('assets/data/books/book.csv')
    d=csv.reader(file)
    data=[]
    for i in d:
        data.append(i)
    if title=='no':
        data.pop(0)
    return data

def ac(val):
    #1ac=100Rs
    #1Rs=0.01Ac
    ans=str(val*(1/93))
    return float(ans[0:4])
    

def get_book_desc(sno,n='f'):
    '''returns the description of a book
n='f' gives full desc or n='o' gives one 1 sentence'''
    file=open('assets/data/books/'+str(sno)+'.txt')
    if n=='f':
        data=file.read()
        return data
    elif n=='o':
        data2=''
        for i in file.read():
            if i=='.':
                return [data2]
            else:
                data2+=i
    

def get_data(username):
    '''returns all the user details'''
    file=open(db)
    d=csv.reader(file)
    data=[]
    for i in d:
        data.append(i)
    if username=='ALL':
        return data
    else:
        for i in data:
            if i[2]==username:
                return i

def try_login(username,password):
    '''Checks if the username and password are matching
retuns 1 if yes'''
    file=open(db)
    data=csv.reader(file)
    for i in data:
        if (i[2]==username and i[4]==password):
            return 1

def add_user(Email,name,username,dob,password):
    ''' Adds new user to database returns 1 if user already exists'''
    a=check_user(username)
    if a==1:
        return 1
    else:
        val=[Email,name,username,dob,password,0]
        print(val)
        file=open(db,'a',newline='\n')
        w=csv.writer(file)
        w.writerow(val)
        file.close()


def open_main():
    import main
