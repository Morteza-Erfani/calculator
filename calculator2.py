import tkinter as tk
from tkinter import E, S, N, W, ttk

window = tk.Tk()

lbl_screen = ttk.Label(
    master= window,
    text= '0',
    font= '30',
)

lbl_screen.grid(
    row = 0,
    column = 0,
    ipady = 30,
    ipadx = 5,
    padx = 1,
    pady = 1,
    columnspan = 4,
    sticky = (E, W),
)

def insert_number(num):
    if lbl_screen['text'] == 'Cannot divided by zero':
        lbl_screen['text'] = '0'
    try:
        if num in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if lbl_screen['text'][-1] != ')':
                if lbl_screen['text'] == '0':
                    lbl_screen['text'] = num
                elif lbl_screen['text'].split(' ')[-1] != '0':
                    lbl_screen['text'] += num
                else:
                    lbl_screen['text'] = lbl_screen['text'][:-1] + num
        elif num == '0' and lbl_screen['text'].split(' ')[-1] != '0':
                lbl_screen['text'] += num
        elif num in ['%' , '/' , '*' , '-' , '+']:
            if lbl_screen['text'][-1] != ' ':
                lbl_screen['text'] += f' {num} '
            else:
                lbl_screen['text'] = lbl_screen['text'][:-3] + f' {num} '
        elif num == '.' and lbl_screen['text'].split(' ')[-1].find('.') == -1:
                if lbl_screen['text'].split(' ')[-1] == '':
                    lbl_screen['text'] += '0' + num    
                else:
                    lbl_screen['text'] += num
        elif num == 'C':
            lbl_screen['text'] = '0'
        elif num == 'CE':
            if lbl_screen['text'][-1] != ' ':
                lbl_screen['text'] = lbl_screen['text'][:-1]
            else:
                lbl_screen['text'] = lbl_screen['text'][:-3]
        elif num == '=':
            if lbl_screen['text'][-1] != ' ':
                if int(eval(lbl_screen['text'])) == float(eval(lbl_screen['text'])):
                    lbl_screen['text'] = str(int(eval(lbl_screen['text'])))
                else: 
                    lbl_screen['text'] = str(eval(lbl_screen['text']))
            else:
                if int(eval(lbl_screen['text'][:-3])) == float(eval(lbl_screen['text'][:-3])):
                    lbl_screen['text'] = str(int(eval(lbl_screen['text'][:-3])))
                else: 
                    lbl_screen['text'] = str(eval(lbl_screen['text'][:-3]))
        elif num == '(':
            if lbl_screen['text'] == '' or lbl_screen['text'][-1] == ' ' or lbl_screen['text'] == '0':
                if lbl_screen['text'][-1] == '0':
                    lbl_screen['text'] = num
                else:
                    lbl_screen['text'] += num
        elif num == ')':
            if lbl_screen['text'].split(' ')[-1].find('(') != -1:
                lbl_screen['text'] += num
            elif lbl_screen['text'].split(' ').find('(') < lbl_screen['text'].split(' ').find(')'):
                lbl_screen['text'] += num
    except ZeroDivisionError:
                lbl_screen['text'] = 'Cannot divided by zero'
    except IndexError:
        pass    

calc_button = [
    {
        'text' : 'C',
        'command' : lambda: insert_number('C'),
    },
    {
        'text' : 'CE',
        'command' : lambda: insert_number('CE'),
    },
    {
        'text' : '%',
        'command' : lambda: insert_number('%'),
    },
    {
        'text' : '/',
        'command' : lambda: insert_number('/'),
    },
    {
        'text' : '(',
        'command' : lambda: insert_number('('),
    },
    {
        'text' : ')',
        'command' : lambda: insert_number(')'),
    },
    {
        'text' : 'Radical',
        'command' : lambda: insert_number('r'),
    },
    {
        'text' : '^',
        'command' : lambda: insert_number('^'),
    },
    {
        'text' : '7',
        'command' : lambda: insert_number('7'),
    },
    {
        'text' : '8',
        'command' : lambda: insert_number('8'),
    },
    {
        'text' : '9',
        'command' : lambda: insert_number('9'),
    },
    {
        'text' : '*',
        'command' : lambda: insert_number('*'),
    },
    {
        'text' : '4',
        'command' : lambda: insert_number('4'),
    },
    {
        'text' : '5',
        'command' : lambda: insert_number('5'),
    },
    {
        'text' : '6',
        'command' : lambda: insert_number('6'),
    },
    {
        'text' : '-',
        'command' : lambda: insert_number('-'),
    },
    {
        'text' : '1',
        'command' : lambda: insert_number('1'),
    },
    {
        'text' : '2',
        'command' : lambda: insert_number('2'),
    },
    {
        'text' : '3',
        'command' : lambda: insert_number('3'),
    },
    {
        'text' : '+',
        'command' : lambda: insert_number('+'),
    },
    {
        'text' : '0',
        'command' : lambda: insert_number('0'),
    },
    {
        'text' : '.',
        'command' : lambda: insert_number('.'),
    },
    {
        'text' : '=',
        'command' : lambda: insert_number('='),
    }
]

calc_button_obj = []

for button in calc_button:
    btn = ttk.Button(
        master = window,
        text = button['text'],
        command = button['command']
    )
    calc_button_obj.append(btn)

btn_row = 1
btn_column = 0

for btn_gr in calc_button_obj:
    if btn_gr['text'] != '=':
        btn_gr.grid(
            row = btn_row,
            column = btn_column, 
            ipady = 20,
            ipadx = 5,
            padx = 1,
            pady = 1,
        )
    else:
        btn_gr.grid(
            row = btn_row,
            column = btn_column, 
            ipady = 20,
            ipadx = 5,
            padx = 1,
            pady = 1,
            columnspan = 2,
            sticky = (E, W),
        )
    if btn_column < 3:
        btn_column += 1
    else:
        btn_row += 1
        btn_column = 0

def bind_func(key):
    if key.keysym in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        insert_number(key.keysym)
    elif key.keysym == 'plus':
        insert_number('+')
    elif key.keysym == 'minus':
        insert_number('-')
    elif key.keysym == 'asterisk':
        insert_number('*')
    elif key.keysym == 'slash':
        insert_number('/')
    elif key.keysym == 'period':
        insert_number('.')
    elif key.keysym == 'percent':
        insert_number('%')
    elif key.keysym == 'Return':
        insert_number('=')
    elif key.keysym == 'BackSpace':
        insert_number('CE')


for btn in calc_button:
    if btn['text'] not in ['C', 'CE', '=']:
        window.bind(btn['text'], bind_func)
    elif btn['text'] == '=':
        window.bind('<Return>', bind_func)
    elif btn['text'] == 'CE':
        window.bind('<BackSpace>', bind_func)


# window.geometry('352x424')
# window.resizable(width=False, height=False)
window.title('2nd Generation Calculator')
window.mainloop()