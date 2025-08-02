from tkinter import *

window = Tk()
window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0, 0)
window.config(bg='white')

bg_image = PhotoImage(file='inventory.png')


titleLabel = Label(window, image=bg_image, compound=LEFT, text='  Inventory Management System',
                   font=('times new roman', 40, 'bold'), bg='#010c48', fg='white', anchor='w', padx=20)
titleLabel.place(x=0, y=0, relwidth=1)

logoutButton = Button(window, text='Logout',
                      font=('timesnew roman', 20, 'bold'), fg='#010c48')
logoutButton.place(x=1100, y=10)

subtitleLabel = Label(
    window, text='Welcome Admin\t\t Date: 08-07-2024\t\t Time: 12:36:17 pm', font=('times new roman', 15), bg='#4d636d', fg='white')
subtitleLabel.place(x=0, y=70, relwidth=1)

leftFrame = Frame(window)
leftFrame.place(x=0, y=102, width=200, height=555)

logoImage = PhotoImage(file='logo.png')
imageLabel = Label(leftFrame, image=logoImage)
imageLabel.pack()

window.mainloop()
