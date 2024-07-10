from tkinter import *
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox,filedialog
import pymysql

#functionality part

#database connection
def connect_database():
    def connect():
        global mycursor,conn
        try:
            conn=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get())
            mycursor=conn.cursor()
            
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try: 
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),'\
                    'address varchar(50),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
            
        messagebox.showinfo('success','Database connection is successfull',parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        
        exitButton.config(state=NORMAL)
        query='select * from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('',END,values=data)
    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+430')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)
    
    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    
    hostEntry=Entry(connectWindow,font=('arial',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)
    
     
    usernameLabel=Label(connectWindow,text='User Name',font=('arial',20,'bold'))
    usernameLabel.grid(row=1,column=0,padx=20)
    
    usernameEntry=Entry(connectWindow,font=('arial',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)
    
     
    passwordLabel=Label(connectWindow,text='Password',font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    
    passwordEntry=Entry(connectWindow,font=('arial',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)
    
    connectButton=ttk.Button(connectWindow,text="Connect",command=connect)
    connectButton.grid(row=3,columnspan=2)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#clock function    
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLable.config(text=f'  Date: {date}\nTime: {currenttime}')
    datetimeLable.after(1000,clock)
 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
#add student button function
def add_student():
    def add_data():
        if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or genderEntry.get()=='' or addressEntry.get()=='' or dobEntry.get()=='':
            messagebox.showerror('Error','All fields are required',parent=add_window)
            
        else:
            
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),
                                        addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
                conn.commit()
                result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    dobEntry.delete(0,END)
                    genderEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=add_window)
                return
            
            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                datalist=list(data)
                studentTable.insert('',END,values=datalist)
                
    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    add_window.title('Add student')
    
    #id label and entry
    idLabel = Label(add_window,text='Id',font=('arial',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('arial',15,'bold'))
    idEntry.grid(row=0,column=1,pady=15,padx=10)
    
    #name label and entry
    nameLabel = Label(add_window,text='Name',font=('arial',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(add_window,font=('arial',15,'bold'))
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    #phoneno label and entry
    phoneLabel = Label(add_window,text='Phone',font=('arial',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(add_window,font=('arial',15,'bold'))
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)
    
    #email Label and entry
    emailLabel = Label(add_window,text='Email',font=('arial',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(add_window,font=('arial',15,'bold'))
    emailEntry.grid(row=3,column=1,pady=15,padx=10)
    
    #address label and entry
    addressLabel = Label(add_window,text='City',font=('arial',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(add_window,font=('arial',15,'bold'))
    addressEntry.grid(row=4,column=1,pady=15,padx=10)
    
    #gender label and entry
    genderLabel = Label(add_window,text='Gender',font=('arial',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(add_window,font=('arial',15,'bold'))
    genderEntry.grid(row=5,column=1,pady=15,padx=10)
    
    #dob label and entry
    dobLabel = Label(add_window,text='DOB',font=('arial',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(add_window,font=('arial',15,'bold'))
    dobEntry.grid(row=6,column=1,pady=15,padx=10)
        
    #add student button
    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=15,)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
#Search student button function
def search_student():
    def search_data():
        query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)
        
    search_window=Toplevel()
    search_window.grab_set()
    search_window.resizable(0,0)
    search_window.title('Search Student')
    
    #id label and entry
    idLabel = Label(search_window,text='Id',font=('arial',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(search_window,font=('arial',15,'bold'))
    idEntry.grid(row=0,column=1,pady=15,padx=10)
    
    #name label and entry
    nameLabel = Label(search_window,text='Name',font=('arial',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(search_window,font=('arial',15,'bold'))
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    #phoneno label and entry
    phoneLabel = Label(search_window,text='Phone',font=('arial',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(search_window,font=('arial',15,'bold'))
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)
    
    #email Label and entry
    emailLabel = Label(search_window,text='Email',font=('arial',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(search_window,font=('arial',15,'bold'))
    emailEntry.grid(row=3,column=1,pady=15,padx=10)
    
    #address label and entry
    addressLabel = Label(search_window,text='City',font=('arial',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(search_window,font=('arial',15,'bold'))
    addressEntry.grid(row=4,column=1,pady=15,padx=10)
    
    #gender label and entry
    genderLabel = Label(search_window,text='Gender',font=('arial',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(search_window,font=('arial',15,'bold'))
    genderEntry.grid(row=5,column=1,pady=15,padx=10)
    
    #dob label and entry
    dobLabel = Label(search_window,text='DOB',font=('arial',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(search_window,font=('arial',15,'bold'))
    dobEntry.grid(row=6,column=1,pady=15,padx=10)
        
    #Search student button
    search_student_button=ttk.Button(search_window,text=' SEARCH',command=search_data)
    search_student_button.grid(row=7,columnspan=2,pady=15,)
    
    
 #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#   
def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    conn.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)
  
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#  
def update_student():
    def update_data():
        query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
        conn.commit()
        messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=update_window)
        update_window.destroy()
        show_student()
    update_window=Toplevel()
    update_window.grab_set()
    update_window.resizable(0,0)
    update_window.title('Update Student')
    
    #id label and entry
    idLabel = Label(update_window,text='Id',font=('arial',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(update_window,font=('arial',15,'bold'))
    idEntry.grid(row=0,column=1,pady=15,padx=10)
    
    #name label and entry
    nameLabel = Label(update_window,text='Name',font=('arial',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(update_window,font=('arial',15,'bold'))
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    #phoneno label and entry
    phoneLabel = Label(update_window,text='Phone',font=('arial',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(update_window,font=('arial',15,'bold'))
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)
    
    #email Label and entry
    emailLabel = Label(update_window,text='Email',font=('arial',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(update_window,font=('arial',15,'bold'))
    emailEntry.grid(row=3,column=1,pady=15,padx=10)
    
    #address label and entry
    addressLabel = Label(update_window,text='City',font=('arial',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(update_window,font=('arial',15,'bold'))
    addressEntry.grid(row=4,column=1,pady=15,padx=10)
    
    #gender label and entry
    genderLabel = Label(update_window,text='Gender',font=('arial',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(update_window,font=('arial',15,'bold'))
    genderEntry.grid(row=5,column=1,pady=15,padx=10)
    
    #dob label and entry
    dobLabel = Label(update_window,text='DOB',font=('arial',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(update_window,font=('arial',15,'bold'))
    dobEntry.grid(row=6,column=1,pady=15,padx=10)
        
    #update student button
    update_student_button=ttk.Button(update_window,text='UPDATE',command=update_data)
    update_student_button.grid(row=7,columnspan=2,pady=15,)
    
    indexing=studentTable.focus()
    
    content=studentTable.item(indexing)
    listdata=content['values']
    
    idEntry.insert(0,listdata[0])
    nameEntry.insert(0,listdata[1])
    phoneEntry.insert(0,listdata[2])
    emailEntry.insert(0,listdata[3])
    addressEntry.insert(0,listdata[4])
    genderEntry.insert(0,listdata[5])
    dobEntry.insert(0,listdata[6])
    
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
#exit button function
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#GUI part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x680+250+250')
root.resizable(0,0  )
root.title('Student Management System')

#datetime on upperleft side
datetimeLable = Label(root,font=('arial',16,'bold'))
datetimeLable.place(x=5,y=5)
clock()

#Top heading
headingLabel = Label(root,text='Student Management System',font=('ariel',28,'italic bold'),width=30)
headingLabel.place(x=200,y=0)


#connect to database button
connectButton = ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=5)

#Left side buttons
leftFrame=Frame(root,)
leftFrame.place(x=50,y=80,width=300,height=600)

#adding logo in left frame
logo_image=PhotoImage(file='C:\sharon(Projects)\project\Student-Management-System/images/students.png')
logo_label=Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

#Buttons
addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=6,column=0,pady=20)

#right frame
rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile','Email','Address','Gender',
                                 'D.O.B','Added date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='City')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Mobile',width=200,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added date',width=150,anchor=CENTER)
studentTable.column('Added Time',width=150,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.heading',font=('arial',12,'bold'))
studentTable.config(show='headings')

root.mainloop()