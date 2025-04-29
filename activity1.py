from tkinter import*
from datetime import date
window = Tk()
window.title("My first App")
window.geometry("500x500")
window.configure(bg="blue")
font_style=("Arial",16)
lbl=Label(text='Hi there',bg='pink',font=font_style)
lbl.pack(pady=10)
e=Entry(font=font_style)
e.pack(pady=10)
def disp():
    name=e.get()
    Message = 'Welcome to my first app \n'
    greet='Hi '+name+"\n"
    t.insert(END,Message)
    t.insert(END,greet)
    t.insert(END,str(date.today())+"\n")
def reset():
   e.delete(0,END)
   t.delete('1.0',END)
btn=Button(text='Click',command=disp,font=font_style)
btn.pack(pady=10)
reset_btn=Button(text="Reset",command=reset,font=font_style)
reset_btn.pack(pady=10)
t=Text(height=5,font=font_style)
t.pack(pady=10)
window.mainloop()