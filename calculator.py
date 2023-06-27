from tkinter import *
import math

r=Tk()
r.title("Adithya's calculator")

#functions
def clr():
    ent.delete(0,END)


def buttonclick(n):
    var=str(ent.get())+str(n)
    ent.delete(0,END)
    ent.insert(0,var)

def add():
    global firstnum
    global fun
    fun="add"
    firstnum=float(ent.get())
    ent.delete(0,END)

def sub():
    global firstnum
    global fun
    fun="sub"
    firstnum=float(ent.get())
    ent.delete(0,END)

def mul():
    global firstnum
    global fun
    fun="mul"
    firstnum=float(ent.get())
    ent.delete(0,END)

def div():
    global firstnum
    global fun
    fun="div"
    firstnum=float(ent.get())
    ent.delete(0,END)

def sqrt():
    global fun
    fun="sqrt"
    ent.delete(0,END)

def eql():
    global secnum
    global res
    secnum=float(ent.get())
    ent.delete(0,END)
    if fun=="add":
        res=firstnum+secnum
    elif fun=="sub":
        res=firstnum-secnum
    elif fun=="div":
        res=firstnum/secnum
    elif fun=="mul":
        res=firstnum*secnum
    elif fun=="sqrt":
        res=math.sqrt(secnum)
            
    ent.insert(0,res)
    

    





#definitions

ent=Entry(r,width=60,borderwidth=5)

button1=Button(r,text="1",padx=40,pady=20,command=lambda:buttonclick(1))
button2=Button(r,text="2",padx=40,pady=20,command=lambda:buttonclick(2))
button3=Button(r,text="3",padx=40,pady=20,command=lambda:buttonclick(3))
button4=Button(r,text="4",padx=40,pady=20,command=lambda:buttonclick(4))
button5=Button(r,text="5",padx=40,pady=20,command=lambda:buttonclick(5))
button6=Button(r,text="6",padx=40,pady=20,command=lambda:buttonclick(6))
button7=Button(r,text="7",padx=40,pady=20,command=lambda:buttonclick(7))
button8=Button(r,text="8",padx=40,pady=20,command=lambda:buttonclick(8))
button9=Button(r,text="9",padx=40,pady=20,command=lambda:buttonclick(9))
button0=Button(r,text="0",padx=40,pady=20,command=lambda:buttonclick(0))
buttondot=Button(r,text=".",padx=40,pady=20,command=lambda:buttonclick('.'))

buttoneql=Button(r,text='=',padx=40,pady=20,command=eql)
buttonclear=Button(r,text="clear",padx=120,pady=20,command=clr)
buttonadd=Button(r,text="+",padx=40,pady=20,command=add)
buttonsub=Button(r,text="-",padx=40,pady=20,command=sub)
buttonmul=Button(r,text="x",padx=40,pady=20,command=mul)
buttondiv=Button(r,text="/",padx=40,pady=20,command=div)
buttonsqrt=Button(r,text="sqrt",padx=40,pady=20,command=sqrt)





#displaying
ent.grid(row=0,column=0,columnspan=4)


button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
buttondiv.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonmul.grid(row=2,column=3)

button7.grid(row=3,column=0)
button8.grid(row=3,column=1)
button9.grid(row=3,column=2)
buttonsub.grid(row=3,column=3)

button0.grid(row=4,column=0)
buttondot.grid(row=4,column=1)
buttoneql.grid(row=4,column=2)
buttonadd.grid(row=4,column=3)

buttonsqrt.grid(row=5,column=3)
buttonclear.grid(row=5,column=0,columnspan=3)

r.mainloop()


