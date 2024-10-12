import tkinter as tk
from tkinter import messagebox, scrolledtext

class Item:
    def __init__(self, name, owner, phone_num):
        self.name = name
        self.owner = owner
        self.phone_num = phone_num

class ItemBook:
    def __init__(self):
        self.items = []
        self.size = 0
    def add_item(self):
        name = name_entry.get()
        owner = owner_entry.get()
        phone_num = phone_num_entry.get()

        for item in self.items:
            if item.name == name and item.owner == owner:
                messagebox.showerror("Error", "物品已经存在，无需重复录入。")
                return

        self.items.append(Item(name, owner, phone_num))
        messagebox.showinfo("Success", "添加完毕。")
        self.clear_entries()
        show_entry_fields("")

    def delete_item(self):
        name = name_entry.get()
        owner = owner_entry.get()

        for i, item in enumerate(self.items):
            if item.name == name and item.owner == owner:
                self.items.pop(i)
                messagebox.showinfo("Success", "删除完毕。")
                self.clear_entries()
                show_entry_fields("")
                return
        messagebox.showerror("Error", "抱歉！您想删除的物品不存在。")

    def show_item(self):
        if not self.items:
            messagebox.showinfo("Info", "物品清单为空！")
            return

        items_str = "\n".join([f"{item.name} {item.owner} {item.phone_num}" for item in self.items])
        item_list_window = tk.Toplevel(root)
        item_list_window.title("物品清单")
        text = scrolledtext.ScrolledText(item_list_window, width=40, height=15)
        text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        text.insert(tk.END, items_str)
        text.config(state=tk.DISABLED)

    def find_item(self):
        name = name_entry.get()
        found = False
        for item in self.items:
            if item.name == name:
                messagebox.showinfo("Found", f"{item.name} {item.owner} {item.phone_num}")
                found = True
        if not found:
            messagebox.showerror("Error", "抱歉！您想查找的物品不存在。")

    def clear_entries(self):
        name_entry.delete(0, tk.END)
        owner_entry.delete(0, tk.END)
        phone_num_entry.delete(0, tk.END)

ib = ItemBook()
def show_entry_fields(action):
    global current_action
    current_action = action
    for widget in input_widgets:
        widget.grid_remove()

    confirm_button.grid_remove()

    if action == "add" or action == "delete":
        name_label.grid(row=2, column=0)
        name_entry.grid(row=2, column=1)
        owner_label.grid(row=3, column=0)
        owner_entry.grid(row=3, column=1)

        if action == "add":
            phone_num_label.grid(row=4, column=0)
            phone_num_entry.grid(row=4, column=1)

    elif action == "find":
        name_label.grid(row=2, column=0)
        name_entry.grid(row=2, column=1)

    confirm_button.grid(row=5, column=0, columnspan=2)

def on_confirm():
    global current_action
    if current_action == "add":
        ib.add_item()
    elif current_action == "delete":
        ib.delete_item()
    elif current_action == "find":
        ib.find_item()
    show_entry_fields("")

def set_action(action):
    global current_action
    current_action = action

def on_add():
    set_action("add")
    show_entry_fields("add")

def on_delete():
    set_action("delete")
    show_entry_fields("delete")

def on_show():
    ib.show_item()

def on_find():
    set_action("find")
    show_entry_fields("find")

root = tk.Tk()
root.title("物品复活系统")

tk.Button(root, text="添加物品", command=on_add).grid(row=0, column=0)
tk.Button(root, text="删除物品", command=on_delete).grid(row=0, column=1)
tk.Button(root, text="显示物品", command=on_show).grid(row=1, column=0)
tk.Button(root, text="查找物品", command=on_find).grid(row=1, column=1)

name_label = tk.Label(root, text="物品名称")
name_entry = tk.Entry(root)

owner_label = tk.Label(root, text="主人名称")
owner_entry = tk.Entry(root)

phone_num_label = tk.Label(root, text="联系方式")
phone_num_entry = tk.Entry(root)

confirm_button = tk.Button(root, text="确认", command=on_confirm)

input_widgets = [name_label, owner_label, phone_num_label, name_entry, owner_entry, phone_num_entry]

current_action = None

root.mainloop()

