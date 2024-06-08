import tkinter as tk
from tkinter import font
import datetime as dt
import os

class item_class:
    def __init__(self, sum, cat='food', date=0):
        self.id = ''
        if date == 0:
            self.date = dt.datetime.now().strftime('%Y-%m-%d')
        else:
            self.date = date
        self.category = cat
        self.sum = sum

    def get_sum(self):
        return self.sum

    def delete(self):
        self.sum = int(self.sum / 10)


class db_class:
    def __init__(self, filename='db.txt'):
        self.db = []
        self.filename = filename

    def load_file(self, filename):
        f = open(filename, 'r')
        for line in f:
            (date, cat, sum) = line.split(' ')
            self.db.append(item_class(sum=float(sum), cat=cat, date=date))
        f.close()

    def write_to_file(self, filename, item):
        f = open(filename, 'a')
        f.write(f'{item.date} {item.category} {item.sum}\n')
        f.close()

    def create_item(self, sum, cat):
        tmp_item = item_class(sum, cat)
        self.db.append(tmp_item)
        self.write_to_file(self.filename, tmp_item)

    def add_item(self, item):
        self.db.append(item)
        self.write_to_file(self.filename, item)

    def get_items(self):
        return [f'{item.date}: {item.category} = {item.sum}' for item in self.db]

    def get_total(self):
        sum = 0
        for item in self.db:
            sum += item.sum
        return sum

def update_label_sum(db, lbl_sum):
    label_sum.config(text = f'summa: {db.get_total()}')
    print(f'new sum: {db.get_total()}')

def update_listbox(db, lb):
    print('Update listbox')
    lb.delete(0, tk.END)
    for item in db.get_items():
        lb.insert(tk.END, item)

def button_add_item_click(window, db, lb_items, itm, lbl_sum):
    db.add_item(itm)
    update_listbox(db, lb_items)
    update_label_sum(db, lbl_sum)
    window.destroy()

def button_cancel_click(window):
    window.destroy()

def button_number_click(number, itm, lbl):
    itm.sum = itm.sum * 10 + number
    lbl.config(text = itm.sum)
    print(itm.sum)

def button_comma_click(itm, lbl):
    pass

def button_delete_click(itm, lbl):
    itm.delete()
    lbl.config(text = itm.get_sum())

def button_category_click(category, item, label):
    item.category = category
    label.config(text = item.category)

def button_show_add_window_click(db, lb_items, lbl_sum):

    def on_closing():
        print("on closing")
    itm = item_class(0)
    window_add = tk.Toplevel(top)
    window_add.geometry('900x800+0+0')
    window_add.title('Add new item')

    window_add.protocol("WM_DELETE_WINDOW", on_closing)

    window_add.rowconfigure(0, minsize=150)
    window_add.rowconfigure(1, minsize=150)
    window_add.rowconfigure(2, minsize=150)
    window_add.rowconfigure(3, minsize=150)
    window_add.rowconfigure(4, minsize=150)
    window_add.rowconfigure(5, minsize=150)
    window_add.rowconfigure(6, minsize=150)
    window_add.columnconfigure(0, minsize=150)
    window_add.columnconfigure(1, minsize=10) # Devider between cateory and numbers
    window_add.columnconfigure(2, minsize=150)
    window_add.columnconfigure(3, minsize=150)
    window_add.columnconfigure(4, minsize=150)
    window_add.columnconfigure(5, minsize=10)
    window_add.columnconfigure(6, minsize=150)

    window_add.wm_attributes("-topmost", True) #always on top
    #window_add.grab_set_global()
    # window_add.protocol("WM_DELETE_WINDOW", lambda: update_listbox(db, lb_items))
    label_info =     tk.Label(window_add, text=itm.sum, font=('Courier New', 30))
    label_category = tk.Label(window_add, text="mat")
    button_add =     tk.Button(window_add, text='Lägg till', font=('Courier New', 20), command=lambda:button_add_item_click(window_add, db, lb_items, itm, lbl_sum))
    button_cancel =  tk.Button(window_add, text='Avbryt', font=('Courier New', 20), command=lambda:button_cancel_click(window_add))

    btn_zero =  tk.Button(window_add, text="0", command=lambda:button_number_click(0, itm, label_info))
    btn_one =   tk.Button(window_add, text="1", command=lambda:button_number_click(1, itm, label_info))
    btn_two =   tk.Button(window_add, text="2", command=lambda:button_number_click(2, itm, label_info))
    btn_three = tk.Button(window_add, text="3", command=lambda:button_number_click(3, itm, label_info))
    btn_four =  tk.Button(window_add, text="4", command=lambda:button_number_click(4, itm, label_info))
    btn_five =  tk.Button(window_add, text="5", command=lambda:button_number_click(5, itm, label_info))
    btn_six =   tk.Button(window_add, text="6", command=lambda:button_number_click(6, itm, label_info))
    btn_seven = tk.Button(window_add, text="7", command=lambda:button_number_click(7, itm, label_info))
    btn_eight = tk.Button(window_add, text="8", command=lambda:button_number_click(8, itm, label_info))
    btn_nine =  tk.Button(window_add, text="9", command=lambda:button_number_click(9, itm, label_info))
    btn_comma =  tk.Button(window_add, text=",", command=lambda:button_comma_click(itm, label_info))
    btn_del =  tk.Button(window_add, text="<-", command=lambda:button_delete_click(itm, label_info))

    btn_food =   tk.Button(window_add, text="mat", command=lambda:button_category_click('mat', itm, label_category))
    btn_coffe =  tk.Button(window_add, text="kaffe", command=lambda:button_category_click('kaffe', itm, label_category))
    btn_bubbel = tk.Button(window_add, text="bubbel", command=lambda:button_category_click('bubbel', itm, label_category))

    # buttons = range(0, 10)
    # for button in buttons:
    #     tk.Button(window_add, text=str(button), command=lambda button=button, itm=itm, label_info=label_info:button_number_click(button, itm, label_info)).grid(row=2, column=button+1)
    label_info.grid(row=0, column=0)
    # label_category.grid(row=0, column=1)
    button_add.grid(    row=1, column=6, rowspan=3, sticky="NSWE")
    button_cancel.grid( row=4, column=6, sticky="NSEW")

    btn_food.grid(  row=1, column=0, sticky="NSEW")
    btn_coffe.grid( row=2, column=0, sticky="NSEW")
    btn_bubbel.grid(row=3, column=0, sticky="NSEW")

    btn_one.grid(   row=1, column=2, sticky="NSEW")
    btn_two.grid(   row=1, column=3, sticky="NSEW")
    btn_three.grid( row=1, column=4, sticky="NSEW")
    btn_four.grid(  row=2, column=2, sticky="NSEW")
    btn_five.grid(  row=2, column=3, sticky="NSEW")
    btn_six.grid(   row=2, column=4, sticky="NSEW")
    btn_seven.grid( row=3, column=2, sticky="NSEW")
    btn_eight.grid( row=3, column=3, sticky="NSEW")
    btn_nine.grid(  row=3, column=4, sticky="NSEW")
    btn_zero.grid(  row=4, column=3, sticky="NSEW")
    btn_del.grid(   row=4, column=4, sticky="NSEW")


if __name__ == '__main__':
    version = '1.0.0'
    author = "Magnus"
    db = db_class()
    db.load_file('db.txt')

    top = tk.Tk()
    # top.attributes('-zoomed', True)
    top.attributes('-topmost', True)
    top.title(f"kvitto registrering, pid: {os.getpid()} v{version}")

    # print(font.families())

    top.rowconfigure(0, minsize=50)
    top.rowconfigure(1, minsize=50)
    top.rowconfigure(2, minsize=100)
    top.rowconfigure(3, minsize=50)

    top.btn_test = tk.Button(top, text="test button")

    var = tk.StringVar(value=db.get_items())
    lb_items = tk.Listbox(top, height=20, width=30, listvariable = var, font=('Courier New', 20))
    lb_items.bind('<<ListboxSelect>>', lambda event:update_listbox(db, event.widget))
    label_sum = tk.Label(top, text=f'summa: {db.get_total()} kr', font=('Courier New', 20))
    button_show_add_window = tk.Button(top, text='add item', font=('Courier New', 20), command=lambda: button_show_add_window_click(db, lb_items, label_sum))

    lb_items.grid(row = 0, column = 0, sticky = 'NSWE')
    label_sum.grid(row = 1, column = 0, sticky = 'NSWE')
    button_show_add_window.grid(row = 2, column = 0, sticky = 'NSWE')
    top.btn_test.grid(row= 3, column = 0, sticky = "NSWE")
    top.mainloop()
