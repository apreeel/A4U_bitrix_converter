from tkinter import *

global data
import urllib.parse
import os

window = Tk()
window.title("Конвертер названий папок сделок в ссылки для Битрикс v0.4")
window.geometry('400x300')


# take name from txt_in, convert to bitrix_link, put it to llb_out and copy to clipboard
def convert():
    url = urllib.parse.quote(txt_in.get())  # convert text to url format
    plus_url = url.replace("%", "+")        # replace all percent to plus chars
    bitrix_link = ('fldr:' + plus_url)      # add "fldr:" prefix
#   print(bitrix_link)                      # console output
    bitrix_var.set(bitrix_link)             # set label with url
    window.clipboard_clear()                # clear clipboard
    window.clipboard_append(bitrix_link)    # copy
    window.update()                         # keep clipboard alive


# check folder
def folder_check():
    txt_2 = txt_in.get()
    fullpath = ('X:\\' + txt_2)
    fullpathlabel.set(fullpath)
    isExist = os.path.exists(fullpath)
    if isExist is True:
        fldr_check_var.set("Folder exists")
    else:
        fldr_check_var.set("Folder does not exist")

# create folder
def folder_create():
    txt_2 = txt_in.get()
    fullpath = ('X:\\' + txt_2)
    fullpathlabel.set(fullpath)
    isExist = os.path.exists(fullpath)
    if isExist is True:
        fldr_check_var.set("Folder exists")
    else:
        fldr_check_var.set("Folder does not exist, creating...")
        os.makedirs(fullpath, exist_ok=True)
        list = ['Рабочие файлы', 'Утвержденный макет', 'Файлы клиента', 'Фото']
        for items in list:
            path = os.path.join(fullpath, items)
            os.mkdir(path)

# def rb_1_sel():

def rb_2_sel():
    actions['1'][1] = not actions['1'][1]
def rb_3_sel():
    actions['2'][1] = not actions['2'][1]

# by pressing GO! button make convert and then check or check and create folder according to chosen radiobutton
def button_press():
    convert()
    for value in actions.values():
        func, should_do = value
        if should_do:
          func()

actions = {
    '1': [folder_check, False],
    '2': [folder_create, False]
}

var = IntVar()
R1 = Radiobutton(window, text="создать ссылку", variable=var, value=1)
R2 = Radiobutton(window, text="и проверить папку", variable=var, value=2, command=rb_2_sel)
R3 = Radiobutton(window, text="и создать, если такой нет", variable=var, value=3, command=rb_3_sel)

# global fullpathlabel
fullpathlabel = StringVar()
# global fldr_check_var
fldr_check_var = StringVar()
fldr_check_var.set("Folder...")
bitrix_var = StringVar()
bitrix_var.set("...")
lbl_out = Label(window, textvariable=bitrix_var)
txt_in = Entry(window, width=20)
lbl = Label(window, text="Тут делаем ссылку для Битрикса")
btn_main = Button(window, text="GO!", command=button_press)
#lbl_2 = Label(window, text="Тут создаём папку на NAS")
#txt_in_2 = Entry(window, width=20)
lbl_3 = Label(window, textvariable=fullpathlabel)
lbl_fldr_check = Label(window, textvariable=fldr_check_var)
#btn_folder_check = Button(window, text="Проверить папку", command=folder_check)
#btn_folder_create = Button(window, text="Создать папку", command=folder_create)


lbl.grid(column=1, row=0)
txt_in.grid(column=1, row=1)
lbl_out.grid(column=1, row=2)
R1.grid(column=0, row=3)
R2.grid(column=1, row=3)
R3.grid(column=2, row=3)
lbl_3.grid(column=1, row=4)
lbl_fldr_check.grid(column=1, row=5)
btn_main.grid(column=1, row=6)

txt_in.focus()
window.mainloop()
