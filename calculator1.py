from cProfile import label
from cgitb import text
import tkinter
from tkinter import *
from turtle import width


screen=Tk()
screen.geometry("570x700")
screen.resizable(False,False)
screen.title("Tawseeq's Calculator")
screen.configure(bg="#17161b")



label_result=Label(screen,width=25,height=2,text="",font=("ariel",30))
label_result.pack()

labeltitle=Label(screen,width=25,height=2,text="Tawseeq's Calculator",font=("chiller",40,'italic bold'),fg="red",bg="green")
labeltitle.place(x=20,y=590)

equation=""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)


Button(screen,width=5,height=1,text="C",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda: clear()).place(x=10,y=100)
Button(screen,width=5,height=1,text="/",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("/")).place(x=150,y=100)
Button(screen,width=5,height=1,text="%",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("%")).place(x=290,y=100)
Button(screen,width=5,height=1,text="*",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("*")).place(x=430,y=100)

Button(screen,width=5,height=1,text="7",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("7")).place(x=10,y=200)
Button(screen,width=5,height=1,text="8",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("8")).place(x=150,y=200)
Button(screen,width=5,height=1,text="9",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("9")).place(x=290,y=200)
Button(screen,width=5,height=1,text="-",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("-")).place(x=430,y=200)

Button(screen,width=5,height=1,text="4",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("4")).place(x=10,y=300)
Button(screen,width=5,height=1,text="5",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("5")).place(x=150,y=300)
Button(screen,width=5,height=1,text="6",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("6")).place(x=290,y=300)
Button(screen,width=5,height=1,text="+",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("+")).place(x=430,y=300)

Button(screen,width=5,height=1,text="1",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("1")).place(x=10,y=400)
Button(screen,width=5,height=1,text="2",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("2")).place(x=150,y=400)
Button(screen,width=5,height=1,text="3",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("3")).place(x=290,y=400)
Button(screen,width=11,height=1,text="0",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show("0")).place(x=10,y=500)

Button(screen,width=5,height=1,text=".",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command= lambda: show(".")).place(x=290,y=500)
Button(screen,width=5,height=3,text="=",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command= lambda: calculate()).place(x=430,y=400)

screen.mainloop()

