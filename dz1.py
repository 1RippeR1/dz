from tkinter import *

root = Tk()

def rename_lable1():
    temp = int(your_ently.get())
    temp2 = int(your_ently2.get())
    label['text'] = f'Ответ{temp+temp2}'
def rename_lable2():
    temp = int(your_ently.get())
    temp2 = int(your_ently2.get())
    label['text'] = f'Ответ{temp - temp2}'
def rename_lable3():
    temp = int(your_ently.get())
    temp2 = int(your_ently2.get())
    label['text'] = f'Ответ{temp / temp2}'
def rename_lable4():
    temp = int(your_ently.get())
    temp2 = int(your_ently2.get())
    label['text'] = f'Ответ{temp * temp2}'

label = Label(width=40, text='Ответ:',)

your_ently = Entry(width=40,bg='blue')
your_ently2 = Entry(width=40,bg='green',fg='white')
your_button1 = Button(text='+',bg='red',command=rename_lable1)
your_button2 = Button(text='-',bg='yellow',command=rename_lable2)
your_button3 = Button(text=':',bg='green',command=rename_lable3)
your_button4 = Button(text='*',bg='green',command=rename_lable4)


your_ently.pack()
your_ently2.pack()
your_button1.pack(side=LEFT)
your_button2.pack(side=LEFT)
your_button3.pack(side=RIGHT)
your_button4.pack(side=RIGHT)
label.pack()
root.mainloop()