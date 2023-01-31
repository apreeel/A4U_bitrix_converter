#name = input("What is your name? ")
#pref_color = input('What is your favourite color? ')
#print(name + ' likes ' + pref_color)

#lb_weight = input('What is your weight in pounds? ')
#kg_weight = float(lb_weight) * 0.45
#print('Your weight is ' + str(kg_weight) + ' kg.')
from tkinter import *
global data
import urllib.parse
#paste text from clipboard to text field
def txt_paste():
    txt_in.delete(0, END)
    global data
    clip_text = window.clipboard_get()
    txt_in.insert(END, clip_text)
#convert text to bitrix format
def convert():
    url = urllib.parse.quote(txt_in.get())
    plus_url = url.replace("%", "+")
    bitrix_link = ('fldr:' + plus_url)
    txt_in.delete(0, END)
    #print(bitrix_link)
    txt_in.insert(END, bitrix_link)
#copy from text field to clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(txt_in.get())
    window.update()
#paste from clipboard, convert, copy to clipboard with a single click
def do_magic():
    txt_in.delete(0, END)               #paste
    global data                         #paste
    clip_text = window.clipboard_get()  #paste
    txt_in.insert(END, clip_text)       #paste

    url = urllib.parse.quote(txt_in.get())  #convert
    plus_url = url.replace("%", "+")        #convert
    bitrix_link = ('fldr:' + plus_url)      #convert
    txt_in.delete(0, END)                   #convert
    txt_in.insert(END, bitrix_link)         #convert

    window.clipboard_clear()                #copy
    window.clipboard_append(txt_in.get())   #copy
    window.update()                         #copy
window = Tk()
window.title("Конвертер названий папок сделок в ссылки для Битрикс v0.1")
window.geometry('250x200')
txt_in = Entry(window, width=20)
lbl = Label(window, text="Вставьте название папки (сделки):")
btn_paste = Button(window, text="Вставить", command=txt_paste)
btn_convert = Button(window, text="Конвертировать", command=convert)
btn_copy = Button(window, text="Скопировать", command=copy_to_clipboard)
btn_magic = Button(window, text="Вжух!", command=do_magic)
lbl.grid(column=0, row=0)
txt_in.grid(column=0, row=1)
btn_paste.grid(column=0, row=2)
btn_convert.grid(column=0, row=3)
btn_copy.grid(column=0, row=4)
btn_magic.grid(column=0, row=5)
txt_in.focus()
window.mainloop()