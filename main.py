from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


class Calculator:
    calculated = True

    def __init__(self, master):
        self.master = master
        self.master.geometry('300x400')
        self.master.title('Calculator')
        self.master.resizable(False, False)

        self.init_gui()

    def init_gui(self):
        self.expression = Label(self.master, text='0', font=('Calibri', 16))
        self.expression.place(relx=0.9, y=20, anchor='ne')

        self.frame_buttons = Frame(self.master)
        self.frame_buttons.place(x=10, y=80, relwidth=1)

        btn_symbols = ['(', ')', 'C', '<-',
                       '1', '2', '3', '+',
                       '4', '5', '6', '-',
                       '7', '8', '9', '*',
                       '0', '.', '=', '/']

        s = ttk.Style()
        s.configure('my.TButton', font=('Calibri', 16))

        for i, symbol in enumerate(btn_symbols):
            btn = ttk.Button(self.frame_buttons, text=symbol, style='my.TButton', width=5)
            btn.grid(row=i // 4, column=i % 4, ipady=10)
            btn.bind('<ButtonRelease-1>', lambda ev, sym=symbol: self.btn_click(sym))

    def btn_click(self, symbol):
        if symbol == '=':
            try:
                self.expression['text'] += '=' + str(eval(self.expression['text']))
                self.calculated = True
            except:
                messagebox.showerror('Ошибка', 'Неверное выражение')
        elif symbol == 'C':
            self.expression['text'] = '0'
            self.calculated = True
        elif symbol == '<-':
            expr = self.expression['text']
            if len(expr) == 1:
                self.expression['text'] = '0'
            else:
                self.expression['text'] = expr[:expr.find('=')]
            self.calculated = False
        else:
            if self.calculated:
                self.expression['text'] = symbol
            else:
                self.expression['text'] += symbol
            self.calculated = False


if __name__ == '__main__':
    root = Tk()
    app = Calculator(root)
    root.mainloop()
