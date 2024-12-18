from tkinter import *

dow = Tk()

dow.title("Test")
dow.geometry("1380x690")
label3 = Label(text = "BLEEEEEEEP",fg = "#A2CFFE",bg ="#A2CFFE",height=5,width = 100,font =("Impact",25))
label3.place(x=0,y=0)
label2 = Label(text = "BLEEEEEEEP",fg = "Green",bg ="Green",height=645,width = 100,font =("Impact",25))
label2.place(x=0,y=100)
label1 = Label(text = "Hi user",fg = "#000000",bg ="#964B00",height=3,width = 25,font =("Impact",25))
label1.pack()


Fr1 = Frame(master=dow,bg="#964B00",height=100,width = 50)

Fr1.pack(side=TOP)

dow.mainloop()

