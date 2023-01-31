from tkinter import *

global data
import urllib.parse
#import pathlib
import os

window = Tk()
window.title("Конвертер названий папок сделок в ссылки для Битрикс v0.2")
window.geometry('450x200')

# paste text from clipboard to text field
def txt_paste():
    txt_in.delete(0, END)
    global data
    clip_text = window.clipboard_get()
    txt_in.insert(END, clip_text)


# convert text to bitrix format
def convert():
    url = urllib.parse.quote(txt_in.get())
    plus_url = url.replace("%", "+")
    bitrix_link = ('fldr:' + plus_url)
    txt_in.delete(0, END)
    # print(bitrix_link)
    txt_in.insert(END, bitrix_link)


# copy from text field to clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(txt_in.get())
    window.update()


# paste from clipboard, convert, copy to clipboard with a single click
def do_magic():
    txt_in.delete(0, END)  # paste
    global data  # paste
    clip_text = window.clipboard_get()  # paste
    txt_in.insert(END, clip_text)  # paste

    url = urllib.parse.quote(txt_in.get())  # convert
    plus_url = url.replace("%", "+")  # convert
    bitrix_link = ('fldr:' + plus_url)  # convert
    txt_in.delete(0, END)  # convert
    txt_in.insert(END, bitrix_link)  # convert

    window.clipboard_clear()  # copy
    window.clipboard_append(txt_in.get())  # copy
    window.update()  # copy


# copy to second text field
def txt_paste_2():
    txt_in_2.delete(0, END)
    global data
    clip_text = window.clipboard_get()
    txt_in_2.insert(END, clip_text)


# check folder
def folder_check():
    txt_2 = txt_in_2.get()
    fullpath = ('X:\\' + txt_2)
    fullpathlabel.set(fullpath)
    isExist = os.path.exists(fullpath)
    if isExist is True:
        fldr_check_var.set("Folder exists")
    else:
        fldr_check_var.set("Folder does not exist")


# create folder
def folder_create():
    txt_2 = txt_in_2.get()
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


global fullpathlabel
fullpathlabel = StringVar()
global fldr_check_var
fldr_check_var = StringVar()
fldr_check_var.set("Folder...")

txt_in = Entry(window, width=20)
lbl = Label(window, text="Тут делаем ссылку для Битрикса")
btn_paste = Button(window, text="Вставить из буфера", command=txt_paste)
btn_convert = Button(window, text="Конвертировать", command=convert)
btn_copy = Button(window, text="Скопировать", command=copy_to_clipboard)
btn_magic = Button(window, text="Вжух!", command=do_magic)
btn_paste_2 = Button(window, text="Вставить из буфера", command=txt_paste_2)

# second row, folder check and create
lbl_2 = Label(window, text="Тут создаём папку на NAS")
txt_in_2 = Entry(window, width=20)
lbl_3 = Label(window, textvariable=fullpathlabel)
btn_folder_check = Button(window, text="Проверить папку", command=folder_check)
btn_folder_create = Button(window, text="Создать папку", command=folder_create)
lbl_fldr_check = Label(window, textvariable=fldr_check_var)

# first row, create bitrix link
lbl.grid(column=0, row=0)
txt_in.grid(column=0, row=1)
btn_paste.grid(column=0, row=3)
btn_convert.grid(column=0, row=4)
btn_copy.grid(column=0, row=5)
btn_magic.grid(column=0, row=6)

# second row, folder check and create with subfolders

lbl_2.grid(column=1, row=0)
txt_in_2.grid(column=1, row=1)
lbl_3.grid(column=1, row=2)
btn_paste_2.grid(column=1, row=3)
btn_folder_check.grid(column=1, row=4)
lbl_fldr_check.grid(column=1, row=5)
btn_folder_create.grid(column=1, row=6)
txt_in.focus()
window.mainloop()
