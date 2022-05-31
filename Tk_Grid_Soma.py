from tkinter import *

#criar a janela/window
janela = Tk()
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.bind('-', lambda event: subtrair())
janela.bind('+', lambda event: soma())
janela.config(background='blue')

#criar a função
def soma():
    if label1['text'] < 10:
        label1['text'] += 1

    else:
        pass

def subtrair():
    if label1['text'] > -10:
        label1['text'] -= 1

    else:
        pass

#criar os widgets
label1 = Label(janela, text=0, font='Arial 24')
bt1 = Button(janela, text='-', font='Arial 20', command=subtrair)
bt2 = Button(janela, text='+', font='Arial 20', command=soma)

#organizar os widgets/layout
bt1.grid(row=0, column=0)
label1.grid(row=0, column=1)
bt2.grid(row=0, column=2)

#executar a janela
janela.mainloop()