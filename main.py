import tkinter as tk
import datetime as dt

class item_class:
    def __init__(self, sum, cat='food'):
        self.id = ''
        self.date = dt.datetime.now().strftime('%Y-%m-%d')
        self.category = cat
        self.sum = sum


class db_class:
    def __init__(self):
        self.db = []
    
    def add_item(self, sum, cat):
        self.db.append(item_class(sum, cat))
    
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

def button_add_item(db):
    db.add_item(sum=213, cat='Food')

def button_add_item_click(window, db, lb_items):
    db.add_item(123, 'Food')
    update_listbox(db, lb_items)
    window.destroy()

def button_number_click(number):
    print(number)

def button_close_click(db, lb_items):
    window_add = tk.Toplevel(top)
    window_add.title('Add new item')
    window_add.wm_attributes("-topmost", True) #always on top
    window_add.grab_set_global() 
    # window_add.protocol("WM_DELETE_WINDOW", lambda: update_listbox(db, lb_items))
    label_info = tk.Label(window_add, text='window add')
    button_add = tk.Button(window_add, text='add', command=lambda:button_add_item_click(window_add, db, lb_items))

    buttons = range(0, 10)
    for button in buttons:
        tk.Button(window_add, text=str(button), command=lambda button=button:button_number_click(button)).grid(row=0, column=button)
    label_info.grid(row=0, column=0)
    button_add.grid(row=1, column=0)


if __name__ == '__main__':
    db = db_class()
    db.add_item(100, 'food')
    db.add_item(123, 'food')
    db.add_item(1024, 'food')

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