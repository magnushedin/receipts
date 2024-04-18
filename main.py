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
    itm.sum = itm.sum * 10 + number
    lbl.config(text = itm.sum)
    print(itm.sum)

def button_category_click(category, item, label):
    item.category = category
    label.config(text = item.category)

def button_show_add_window_click(db, lb_items):
    itm = item_class(0)
    window_add = tk.Toplevel(top)
    window_add.geometry('400x400')
    window_add.title('Add new item')
    window_add.wm_attributes("-topmost", True) #always on top
    window_add.grab_set_global() 
    # window_add.protocol("WM_DELETE_WINDOW", lambda: update_listbox(db, lb_items))
    label_info =     tk.Label(window_add, text=itm.sum)
    label_category = tk.Label(window_add, text="choose a category")
    button_add =     tk.Button(window_add, text='add', command=lambda:button_add_item_click(window_add, db, lb_items, itm))

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

    btn_food =   tk.Button(window_add, text="food", command=lambda:button_category_click('food', itm, label_category))
    btn_coffe =  tk.Button(window_add, text="coffé", command=lambda:button_category_click('coffé', itm, label_category))
    btn_bubbel = tk.Button(window_add, text="bubbel", command=lambda:button_category_click('bubbel', itm, label_category))

    # buttons = range(0, 10)
    # for button in buttons:
    #     tk.Button(window_add, text=str(button), command=lambda button=button, itm=itm, label_info=label_info:button_number_click(button, itm, label_info)).grid(row=2, column=button+1)
    label_info.grid(    row=0, column=0)
    label_category.grid(row=0, column=1)
    button_add.grid(    row=1, column=0)
    
    btn_food.grid(  row=2, column=0)
    btn_coffe.grid( row=3, column=0)
    btn_bubbel.grid(row=4, column=0)

    btn_one.grid(   row=3, column=1)
    btn_two.grid(   row=3, column=2)
    btn_three.grid( row=3, column=3)
    btn_four.grid(  row=4, column=1)
    btn_five.grid(  row=4, column=2)
    btn_six.grid(   row=4, column=3)
    btn_seven.grid( row=5, column=1)
    btn_eight.grid( row=5, column=2)
    btn_nine.grid(  row=5, column=3)
    btn_zero.grid(  row=6, column=2)


if __name__ == '__main__':
    db = db_class()
    db.load_file('db.txt')

    top = tk.Tk()
    top.title("kvitto registrering")

    var = tk.StringVar(value=db.get_items())
    lb_items = tk.Listbox(top, height=30, width=30, listvariable = var)
    lb_items.bind('<<ListboxSelect>>', lambda event:update_listbox(db, event.widget))
    button_show_add_window = tk.Button(top, text='add item', command=lambda: button_show_add_window_click(db, lb_items))
    label_sum = tk.Label(top, text=f'summa: {db.get_total()} kr')

    lb_items.grid(row = 0, column = 0, sticky = 'W')
    label_sum.grid(row = 1, column = 0, sticky = 'W')
    button_show_add_window.grid(row = 2, column = 0, sticky = 'W')
    top.mainloop()