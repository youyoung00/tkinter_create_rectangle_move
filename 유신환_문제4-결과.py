from tkinter import *

window = Tk()

Label(window, text="대학명:").grid(row=0)
Label(window, text="단과대학:").grid(row=1)
Label(window, text="학과:").grid(row=2)
Label(window, text="학번:").grid(row=3) 
Label(window, text="성명:").grid(row=4)
Label(window, text="").grid(row=5)

e1 = Entry(window)
e2 = Entry(window)
e3 = Entry(window)
e4 = Entry(window)
e5 = Entry(window)

e1.grid(row=0, column=1, columnspan=3) 
e2.grid(row=1, column=1, columnspan=3)
e3.grid(row=2, column=1, columnspan=3) 
e4.grid(row=3, column=1, columnspan=3)
e5.grid(row=4, column=1, columnspan=3) 

label = Label(window)
label.grid(row=5, column=5) 

Button(window, text='삭제').grid(row=5, column=1, columnspan=2) 
Button(window, text='제출').grid(row=5, column=2, columnspan=2) 

window.mainloop( )