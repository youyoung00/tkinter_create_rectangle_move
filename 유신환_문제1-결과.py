from tkinter import *
window = Tk()
window.title("2021-2학기 SW프로그래밍입문 메인과제2-1")
w = Canvas(window, width=500, height=500)
w.pack()
left = 50
top = 50
right = 100
bottom = 100


w.create_rectangle(left, top, right, bottom, fill="yellow")

def movRight():
    w.delete(ALL)
    global left
    global top
    global right
    global bottom
    
    left = left + 5
    right = right + 5

    w.create_rectangle(left, top, right, bottom, fill="yellow")
    
def movLeft():
    w.delete(ALL)
    global left
    global top
    global right
    global bottom
    
    left = left - 5
    right = right - 5
    
    w.create_rectangle(left, top, right, bottom, fill="yellow")
    
def movTop():
    w.delete(ALL)
    global left
    global top
    global right
    global bottom
    
    top = top - 5
    bottom = bottom - 5

    w.create_rectangle(left, top, right, bottom, fill="yellow")
    
def movBottom():
    w.delete(ALL)
    global left
    global top
    global right
    global bottom
    
    top = top + 5
    bottom = bottom + 5

    w.create_rectangle(left, top, right, bottom, fill="yellow")
    
Button(window, text="<==(좌)", bg="red",fg="black",
       command=movLeft).pack(side=LEFT)
Button(window, text="==>(우)", bg="green", fg="black",
       command=movRight).pack(side=LEFT)
Button(window, text="^(상)", bg="orange", fg="black",
       command=movTop).pack(side=LEFT)
Button(window, text="v(하)", bg="orange", fg="black",
       command=movBottom).pack(side=LEFT)


window.mainloop()
