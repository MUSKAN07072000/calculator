from tkinter import *
from tkinter import font

root = Tk()
root.title("calculator")
root.geometry("400x600")
root.configure( bg = "#25c49f")

#FOR ENTRY
entry_value = StringVar()
entry_value.set("")
entry = Entry(root, textvariable = entry_value , relief = RAISED , bd = 8 , font = "Copperplate" )
entry.pack(ipadx = 140 , ipady = 20 , padx = 20 , pady = 20)

#BINDING BUTTONS WITH EVENTS
def click(event):
    global entry_value
    text = event.widget.cget("text")
    if text == "=":
        if entry_value.get().isdigit():
            value = int(entry_value.get())
        else:
            value = eval(entry.get())
        entry_value.set(value)
        entry.update()

    elif text == "C":
        entry_value.set("")
        entry.update()
    else:
        entry_value.set(entry_value.get() + text)
        entry.update()



#COMMAND OF BUTTONS
def b9():
    print(9)
def b8():
    print(8)
def b7():
    print(7)
def b6():
    print(6)
def b5():
    print(5)
def b4():
    print(4)
def b3():
    print(3)
def b2():
    print(2)
def b1():
    print(1)
def b0():
    print(0)
def bs():
    print("-")
def ba():
    print("+")
def bc():
    print("C")
def bp():
    print("%")
def bm():
    print("*")
def bd():
    print("/")
def be():
    print("=")

#FRAMING BUTTONS

frame = LabelFrame(root ,  padx = 2 , pady = 2 , height = 5 , width = 10, bg = "#25c49f")
b9 = Button(frame , text = "9" , command = b9 , height = 5, width = 10, relief = RAISED , bg = "#47b39a",bd = 5)
b8 = Button(frame , text = "8" , command = b8, height = 5, width = 10, relief = RAISED, bg = "#47b39a",bd = 5)
b7 = Button(frame , text = "7" , command = b7, height = 5, width = 10, relief = RAISED, bg ="#47b39a",bd = 5)
bc = Button(frame , text = "C" , command = b7, height = 5, width = 10, relief = RAISED, bg ="#47b39a",bd = 5)
frame.pack(expand = "yes" , fill = "both")

frame = LabelFrame(root ,  padx = 2, pady = 2, height = 5 , width = 10, bg = "#25c49f")
b6 = Button(frame , text = "6" , command = b6, height = 5, width = 10, relief = RAISED, bg ="#47b39a",bd = 5)
b5 = Button(frame , text = "5" , command = b5, height = 5, width = 10, relief = RAISED, bg = "#47b39a",bd = 5)
b4 = Button(frame , text = "4" , command = b4, height = 5, width = 10, relief = RAISED, bg = "#47b39a",bd = 5)
bp = Button(frame , text = "%" , command = bp, height = 5, width = 10, relief = RAISED, bg ="#47b39a",bd = 5)
frame.pack(expand = "yes" , fill = "both")

frame = LabelFrame(root ,  padx = 2 , pady = 2, height =5 , width = 10, bg = "#25c49f")
b3 = Button(frame , text = "3" , command = b3, height = 5, width = 10, relief = RAISED, bg = "#47b39a",bd = 5)
b2 = Button(frame , text = "2" , command = b2, height = 5, width = 10, relief = RAISED, bg = "#47b39a",bd = 5)
b1 = Button(frame , text = "1" , command = b1, height = 5, width = 10, relief = RAISED, bg = "#47b39a",bd =5)
bm= Button(frame , text = "*" , command = bm, height = 5, width = 10, relief = RAISED, bg ="#47b39a",bd = 5)
frame.pack(expand = "yes" , fill = "both")

frame = LabelFrame(root ,  padx = 6, pady = 2 , height =5 , width = 10 , bg = "#25c49f")
b0 = Button(frame , text = "0" , command = b0, height = 5, width = 9, relief = RAISED, bg = "#47b39a",bd = 5)
bs = Button(frame , text = "-" , command = bs, height = 5, width = 8, relief = RAISED, bg = "#47b39a",bd = 5)
ba = Button(frame , text = "+" , command = ba, height = 5, width = 8, relief = RAISED, bg = "#47b39a",bd = 5)
bd = Button(frame , text = "/" , command = bd, height = 5, width = 8, relief = RAISED, bg ="#47b39a",bd = 5)
be = Button(frame , text = "=" , command = be, height = 5, width = 8, relief = RAISED, bg ="#47b39a",bd = 5)
frame.pack(expand = "yes" , fill = "both")

#CHANGING FONT OF BUTTON TEXT
myfont = font.Font(size = 9 , weight = 'bold')
b9['font'] = myfont
b8['font'] = myfont
b7['font'] = myfont
bc['font'] = myfont
b6['font'] = myfont
b5['font'] = myfont
b4['font'] = myfont
bp['font'] = myfont
b3['font'] = myfont
b2['font'] = myfont
b1['font'] = myfont
bm['font'] = myfont
b0['font'] = myfont
bs['font'] = myfont
ba['font'] = myfont
bd['font'] = myfont
be['font'] = myfont


#PACKING BUTTONS

b9.pack(side = LEFT , padx = 6 , pady = 2)
b8.pack(side = LEFT, padx = 6, pady = 2)
b7.pack(side = LEFT, padx = 6, pady = 2)
bc.pack(side = LEFT, padx = 6 , pady = 2)
b6.pack(side = LEFT, padx = 6 , pady = 2)
b5.pack(side = LEFT, padx = 6 , pady = 2)
b4.pack(side = LEFT, padx = 6 , pady = 2)
bp.pack(side = LEFT, padx = 6, pady = 2)
b3.pack(side = LEFT, padx = 6 , pady = 2)
b2.pack(side = LEFT, padx = 6 , pady = 2)
b1.pack(side = LEFT, padx = 6 , pady = 2)
bm.pack(side = LEFT, padx = 6 , pady = 2)
b0.pack(side = LEFT, padx = 2 , pady = 2)
bs.pack(side = LEFT, padx = 2 , pady = 2)
ba.pack(side = LEFT, padx = 2 , pady = 2)
bd.pack(side = LEFT, padx =2 , pady = 2)
be.pack(side = LEFT, padx =2 , pady = 2)

#BINDING BUTTONS
b9.bind("<Button-1>" , click)
b8.bind("<Button-1>" , click)
b7.bind("<Button-1>" , click)
b6.bind("<Button-1>" , click)
b5.bind("<Button-1>" , click)
b4.bind("<Button-1>" , click)
b3.bind("<Button-1>" , click)
b2.bind("<Button-1>" , click)
b1.bind("<Button-1>" , click)
b0.bind("<Button-1>" , click)
bs.bind("<Button-1>" , click)
ba.bind("<Button-1>" , click)
bc.bind("<Button-1>" , click)
bp.bind("<Button-1>" , click)
bm.bind("<Button-1>" , click)
bd.bind("<Button-1>" , click)
be.bind("<Button-1>" , click)

root.mainloop()











