import tkinter as tk
from tkinter import messagebox

class Item:
    def __init__(self, name, owner, phone_num):
        self.name = name
        self.owner = owner
        self.phone_num = phone_num

class ItemBook:
    def __init__(self):
        self.items = []

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

    def delete_item(self):
        name = name_entry.get()
        owner = owner_entry.get()

        for i, item in enumerate(self.items):
            if item.name == name and item.owner == owner:
                self.items.pop(i)
                messagebox.showinfo("Success", "删除完毕。")
                return
        messagebox.showerror("Error", "抱歉！您想删除的物品不存在。")

    def show_item(self):
        if not self.items:
            messagebox.showinfo("Info", "物品清单为空！")
            return

        items_str = "\n".join([f"{item.name} {item.owner} {item.phone_num}" for item in self.items])
        messagebox.showinfo("Items", items_str)

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

def add_item():
    ib.add_item()

def delete_item():
    ib.delete_item()

def show_item():
    ib.show_item()

def find_item():
    ib.find_item()

root = tk.Tk()
root.title("物品交换系统")

tk.Label(root, text="物品名称").grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="主人名称").grid(row=1, column=0)
owner_entry = tk.Entry(root)
owner_entry.grid(row=1, column=1)

tk.Label(root, text="联系方式").grid(row=2, column=0)
phone_num_entry = tk.Entry(root)
phone_num_entry.grid(row=2, column=1)

tk.Button(root, text="添加物品", command=add_item).grid(row=3, column=0)
tk.Button(root, text="删除物品", command=delete_item).grid(row=3, column=1)

tk.Button(root, text="显示物品", command=show_item).grid(row=4, column=0)
tk.Button(root, text="查找物品", command=find_item).grid(row=4, column=1)

root.mainloop()

ib = ItemBook()