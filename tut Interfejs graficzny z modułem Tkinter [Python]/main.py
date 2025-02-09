import tkinter



root = tkinter.Tk()
root.geometry('480x480')
label1 = tkinter.Label(root, text="Aplikacja")
label1.pack()

def btnFn():
    print("clicket")

btn1 = tkinter.Button(root, text="Przysick1",width=10,bg='red',fg='white', command=btnFn)
btn1.pack(side=tkinter.RIGHT)
btn2 = tkinter.Button(root, text="Przysick2", command=btnFn)
btn2.pack(side=tkinter.BOTTOM)
btn3 = tkinter.Button(root, text="Przysick3", command=btnFn)
btn3.place(x=200,y=200)

root.mainloop()