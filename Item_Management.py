import tkinter as tk
from tkinter import ttk
from Item_Class import ItemBook  # 导入ItemBook类

# 初始化ItemBook实例
ib = ItemBook()

def switch_frame(frame):
    frame.tkraise()

def item_process_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    # 添加物品按钮,查找物品按钮，显示所有物品按钮,删除物品按钮
    tk.Button(frame, text="添加物品", command=lambda: switch_frame(add_frame(root))).grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    tk.Button(frame, text="查找物品", command=lambda: switch_frame(find_frame(root))).grid(row=0, column=1, sticky="ew", padx=5, pady=5)
    tk.Button(frame, text="显示所有物品", command=lambda: switch_frame(show_frame(root))).grid(row=0, column=2, sticky="ew", padx=5, pady=5)
    tk.Button(frame, text="删除物品", command=lambda: switch_frame(delete_frame(root))).grid(row=0, column=3, sticky="ew", padx=5, pady=5)

    return frame

# 添加物品页面
def add_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    # 选择类型后更新属性显示
    def update_attributes_display(event=None):
        selected_category = type_combobox.get()
        if selected_category:
            attributes = ib.load_attributes().get(selected_category, [])
            attributes_label.config(text="待填入属性： " + ", ".join(attributes))
        else:
            attributes_label.config(text="待填入属性：")

    tk.Label(frame, text="物品名:").grid(row=1, column=0, sticky="e")
    entry_item_name = tk.Entry(frame)
    entry_item_name.grid(row=1, column=1)

    tk.Label(frame, text="物品描述:").grid(row=2, column=0, sticky="e")
    entry_item_description = tk.Entry(frame)
    entry_item_description.grid(row=2, column=1)

    tk.Label(frame, text="地址:").grid(row=3, column=0, sticky="e")
    entry_item_location = tk.Entry(frame)
    entry_item_location.grid(row=3, column=1)

    tk.Label(frame, text="用户电话:").grid(row=4, column=0, sticky="e")
    entry_item_contact_phone = tk.Entry(frame)
    entry_item_contact_phone.grid(row=4, column=1)

    tk.Label(frame, text="邮箱:").grid(row=5, column=0, sticky="e")
    entry_item_email = tk.Entry(frame)
    entry_item_email.grid(row=5, column=1)

    tk.Label(frame, text="选择类型:").grid(row=6, column=0, sticky="e")
    type_combobox = ttk.Combobox(frame, values=list(ib.load_attributes().keys()))
    type_combobox.grid(row=6, column=1, columnspan=2)
    type_combobox.bind("<<ComboboxSelected>>", update_attributes_display)

    attributes_label = tk.Label(frame, text="待填入属性：")
    attributes_label.grid(row=7, column=0, columnspan=2)

    tk.Label(frame, text="属性(空格分隔):").grid(row=8, column=0, sticky="e")
    keys_entry = tk.Entry(frame)
    keys_entry.grid(row=8, column=1)

    tk.Button(frame, text="确认添加物品", command=lambda: ib.add_item(
        entry_item_name.get(),
        entry_item_description.get(),
        entry_item_location.get(),
        entry_item_contact_phone.get(),
        entry_item_email.get(),
        type_combobox.get(),
        keys=None if keys_entry.get() == '' else keys_entry.get().split()
    )).grid(row=9, column=0, columnspan=2)

    frame.entries = [entry_item_name, entry_item_description, entry_item_location, entry_item_contact_phone, entry_item_email, type_combobox, keys_entry]

    tk.Button(frame, text="返回", command=lambda: switch_frame(item_process_frame(root))).grid(row=10, column=0, columnspan=2)
    return frame

# 查找物品页面
def find_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="选择类型:").grid(row=0, column=0, sticky="e")
    type_combobox = ttk.Combobox(frame, values=list(ib.load_attributes().keys()))
    type_combobox.grid(row=0, column=1, columnspan=2)

    tk.Label(frame, text="输入物品名:").grid(row=1, column=0, sticky="e")
    entry_item_name = tk.Entry(frame)
    entry_item_name.grid(row=1, column=1)

    tk.Label(frame, text="输入用户名:").grid(row=2, column=0, sticky="e")
    entry_item_keyword = tk.Entry(frame)
    entry_item_keyword.grid(row=2, column=1)

    tk.Button(frame, text="确认", command=lambda: ib.find_item(entry_item_name.get(), entry_item_keyword.get(), type_combobox.get())).grid(row=3, column=1, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(item_process_frame(root))).grid(row=4, column=1, columnspan=2)
    return frame

# 显示物品页面
def show_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    tk.Button(frame, text="显示所有物品", command=ib.show_item).grid(row=0, column=0, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(item_process_frame(root))).grid(row=1, column=0, columnspan=2)
    return frame

# 删除物品页面
def delete_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="选择类型:").grid(row=0, column=0, sticky="e")
    type_combobox = ttk.Combobox(frame, values=list(ib.load_attributes().keys()))
    type_combobox.grid(row=0, column=1, columnspan=2)

    tk.Label(frame, text="输入物品名:").grid(row=1, column=0, sticky="e")
    entry_item_name = tk.Entry(frame)
    entry_item_name.grid(row=1, column=1)

    tk.Button(frame, text="确认删除", command=lambda: ib.delete_item(entry_item_name.get(), type_combobox.get())).grid(row=2, column=0, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(item_process_frame(root))).grid(row=3, column=0, columnspan=2)
    return frame

def start_item_management():
    root = tk.Tk()
    root.title("物品管理系统")
    frame = item_process_frame(root)
    frame.tkraise()
    root.mainloop()

#if __name__ == "__main__":
    #start_item_management()









