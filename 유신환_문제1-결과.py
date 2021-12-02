from tkinter import *
window = Tk()
window.title("2021-2학기 SW프로그래밍입문 메인과제2-1")
w = Canvas(window, width=500, height=500)
w.pack()
w.create_rectangle(50, 50, 100, 100, fill="yellow")

def movRight():
    w.create_rectangle(55, 50, 105, 100, fill="yellow")
    
def movLeft():
    w.create_rectangle(50, 50, 100, 100, fill="yellow")
    
def movTop():
    w.create_rectangle(50, 50, 100, 100, fill="yellow")
    
def movBottom():
    w.create_rectangle(50, 50, 100, 100, fill="yellow")
    
Button(window, text="<==(좌)", bg="red",fg="black", command=movLeft).pack(side=LEFT)
Button(window, text="==>(우)", bg="green", fg="black", command=movRight).pack(side=LEFT)
Button(window, text="^(상)", bg="orange", fg="black", command=movTop).pack(side=LEFT)
Button(window, text="v(하)", bg="orange", fg="black", command=movBottom).pack(side=LEFT)


window.mainloop()