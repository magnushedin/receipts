import tkinter as tk
import datetime as dt

class item_class:
    def __init__(self, sum, cat='food', date=0):
        self.id = ''
        if date == 0:
            self.date = dt.datetime.now().strftime('%Y-%m-%d')
        else:
            self.date = date
        self.category = cat
        self.sum = sum


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

def update_listbox(db, lb):
    print('Update listbox')
    lb.delete(0, tk.END)
    for item in db.get_items():
        lb.insert(tk.END, item)

def button_add_item_click(window, db, lb_items, itm):
    db.add_item(itm)
    update_listbox(db, lb_items)
    window.destroy()

def button_number_click(number, itm, lbl):
    itm.sum += number
    lbl.config(text = itm.sum)
    print(itm.sum)

def button_close_click(db, lb_items):
    itm = item_class(0)
    window_add = tk.Toplevel(top)
    window_add.title('Add new item')
    window_add.wm_attributes("-topmost", True) #always on top
    window_add.grab_set_global() 
    # window_add.protocol("WM_DELETE_WINDOW", lambda: update_listbox(db, lb_items))
    label_info = tk.Label(window_add, text=itm.sum)
    button_add = tk.Button(window_add, text='add', command=lambda:button_add_item_click(window_add, db, lb_items, itm))

    buttons = range(0, 10)
    for button in buttons:
        tk.Button(window_add, text=str(button), command=lambda button=button, itm=itm, label_info=label_info:button_number_click(button, itm, label_info)).grid(row=2, column=button+1)
    label_info.grid(row=0, column=0)
    button_add.grid(row=1, column=0)


if __name__ == '__main__':
    db = db_class()
    db.load_file('db.txt')

    top = tk.Tk()

    var = tk.StringVar(value=db.get_items())
    lb_items = tk.Listbox(top, height=30, width=30, listvariable = var)
    lb_items.bind('<<ListboxSelect>>', lambda event:update_listbox(db, event.widget))
    button_close = tk.Button(top, text='add item', command=lambda: button_close_click(db, lb_items))
    label_sum = tk.Label(top, text=f'summa: {db.get_total()} kr')

    lb_items.grid(row = 0, column = 0, sticky = 'W')
    label_sum.grid(row = 1, column = 0, sticky = 'W')
    button_close.grid(row = 2, column = 0, sticky = 'W')
    top.mainloop()