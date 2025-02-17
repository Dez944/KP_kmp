from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def chenge_fonts(fontss):
    text_fild['font'] = fonts[fontss]['font']

def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()

def save_file():
    file_path = filedialog.asksaveasfilename()
    with open(file_path) as f:
        text = text_fild.get('1.0', END)
        f.write(text)


root = Tk()
root.title('Ntpd')
root.geometry('450x400')

main_menu = Menu(root)

file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

view_menu = Menu(main_menu, tearoff=0)
view_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub = Menu(view_menu, tearoff=0)
font_menu_sub.add_command(label='Arial', command=lambda: chenge_fonts('Arial'))
font_menu_sub.add_command(label='Comic Sans MS', command=lambda: chenge_fonts('CSMS'))
view_menu.add_cascade(label='Шрифт..', menu=font_menu_sub)
root.config(menu=view_menu)

main_menu.add_cascade(label='Файл', menu=file_menu)
main_menu.add_cascade(label='Текст', menu=view_menu)
root.config(menu=main_menu)

f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

fonts = {'Arial': {'font': 'Arial 14'},
    'CSMS': {'font': ('Comic Sans MS', 14)}}

text_fild = Text(f_text, wrap=WORD, font='Arial 14')
text_fild.pack(expand=1, fill=BOTH, side=LEFT)

root.mainloop()