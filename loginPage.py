from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='sharon' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success','Login successful')
        root.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Please enter correct credentials')

root=Tk()

root.geometry('1280x700+250+250')
root.title('Login System of Student Management System')
root.resizable(False,False)
backgroundImage = ImageTk.PhotoImage(file='C:\sharon(Projects)\project\Student-Management-System/images/bg.jpg')
bgLabel = Label(root,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame = Frame(root,bg='white')
loginFrame.place(x=400,y=150)

logoImage = PhotoImage(file='C:\sharon(Projects)\project\Student-Management-System/images/logo.png')

logoLabel = Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage = PhotoImage(file='C:\sharon(Projects)\project\Student-Management-System/images/user.png')
usernameLabel = Label(loginFrame,image=usernameImage,text='Username',compound=LEFT,
                      font = ('arial',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry = Entry(loginFrame,font = ('arial',20,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordImage = PhotoImage(file='C:\sharon(Projects)\project\Student-Management-System/images/password.png')
passwordLabel = Label(loginFrame,image=passwordImage,text='Password',compound=LEFT,
                      font = ('arial',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry = Entry(loginFrame,font = ('arial',20,'bold'),bd=5,show='*')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)


loginButton = Button(loginFrame,text='Login',font=('arial',14,'bold'),width = 15,
                     fg = 'white',bg = 'cornflowerblue',activebackground='cornflowerblue',
                     activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=10)



root.mainloop()
