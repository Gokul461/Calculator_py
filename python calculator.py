from tkinter import *
import ast
root = Tk()
root.config(bg='black')
root.resizable(False,False)
i = 0
def get_num(num):
    global i
    display.insert(i,num)
    i+=1
def get_operation(ope):
    global i
    display.insert(i,ope)
    i+=len(ope)
def clearall():
    display.delete(0,END)
def calculate():
    e_str= display.get()
    try:
        node = ast.parse(e_str, mode='eval')
        res = eval(compile(node, '<string>', 'eval'))
        clearall()
        display.insert(0, res)
    except Exception:
        clearall()
        display.insert(0,"ERROR")
def backspace():
    global i
    l = display.get()
    if len(l) != 0:
        new = l[:-1]
        clearall()
        display.insert(0,new)
    else:
        clearall()
        display.insert(0,"")

display = Entry(root)
display.grid(row=0,columnspan=6)
#button for numbers
numbers=[1,2,3,4,5,6,7,8,9]
counter = 0
for i in range(3):
    for j in range(3):
        but_text = numbers[counter]
        butt = Button(root,text=but_text,width=4,height=2,fg='white',bg='black',command = lambda text = but_text:get_num(text))
        butt.grid(row=i+2,column=j)
        counter+=1
#button for 0
butt1 = Button(text=0,width=4,height=2,fg='white',bg='black',command = lambda text1=0 :get_num(text1))
butt1.grid(row=5,column=1)
#button for operators
count=0
ops = ["+","-","*","/","%","*3.14","(",")","**","**2"]
for i in range(4):
    for j in range(3):
        if count < len(ops):
            op = ops[count]
            butt3 = Button(root,text=op,fg='white',bg='black',width=4,height=2,command = lambda text = op:get_operation(text))
            count += 1
            butt3.grid(row=i+2,column=j+3)
ac = Button(root,text="AC",width=4,height=2,fg='white',bg='black',command=clearall)
ac.grid(row=5,column=0)
Equal = Button(root,text="=",width=4,height=2,fg='white',bg='black',command=calculate)
Equal.grid(row=5,column=5)
back = Button(root,text='<-',width=4,fg='white',bg='black',height=2,command=backspace)
back.grid(row=5,column=4)
dot = Button(root,text=".",width=4,fg='white',bg='black',height=2,command = lambda text1='.' :get_num(text1))
dot.grid(row=5,column=2)
root.mainloop()