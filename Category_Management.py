import tkinter as tk
from tkinter import ttk
from Category_Class import ItemCategory

ic = ItemCategory()
def switch_frame(frame):
    frame.tkraise()


def category_process_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    tk.Button(frame, text="添加类型", command=lambda: switch_frame(add_category_frame(root))).grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    tk.Button(frame, text="修改类型", command=lambda: switch_frame(modify_category_frame(root))).grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    tk.Button(frame, text="显示所有类型", command=lambda: switch_frame(show_category_frame(root))).grid(row=3, column=0, sticky="ew", padx=5, pady=5)
    return frame


def add_category_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    # 添加物品类别
    tk.Label(frame, text="添加物品类别:").grid(row=1, column=0, sticky="e")
    entry_category_name = tk.Entry(frame)  # 局部变量
    entry_category_name.grid(row=1, column=1)
    tk.Label(frame, text="添加属性（空格分隔）:").grid(row=2, column=0, sticky="e")
    entry_category_attributes = tk.Entry(frame)  # 局部变量
    entry_category_attributes.grid(row=2, column=1)
    tk.Button(frame, text="确认", command=lambda: ic.add_category(entry_category_name.get(), [attr.strip() for attr in entry_category_attributes.get().split() if attr.strip()])).grid(row=3, column=1, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(category_process_frame(root))).grid(row=4, column=1, columnspan=2)
    return frame


def modify_category_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    # 获取所有类别名称
    def get_all_categories_names():
        return [category.name for category in ic.get_all_categories()]

    # 更新属性显示
    def update_attributes_display(event=None):
        selected_category = type_combobox.get()
        if selected_category:
            attributes = ic.categories[selected_category].get_attributes()
            attributes_label.config(text="原有属性： " + ", ".join(attributes))

    # 修改物品类别
    tk.Label(frame, text="当前物品类别名称:").grid(row=1, column=0, sticky="e")
    type_combobox = ttk.Combobox(frame, values=get_all_categories_names())
    type_combobox.grid(row=1, column=1, columnspan=2)
    type_combobox.bind("<<ComboboxSelected>>", update_attributes_display)  # 绑定事件

    tk.Label(frame, text="新物品类别名称:").grid(row=2, column=0, sticky="e")
    entry_new_category_name = tk.Entry(frame)
    entry_new_category_name.grid(row=2, column=1)

    attributes_label = tk.Label(frame, text="原有属性：")
    attributes_label.grid(row=3, column=0, columnspan=2)

    tk.Label(frame, text="添加新属性（空格分隔）:").grid(row=4, column=0, sticky="e")
    entry_category_attributes = tk.Entry(frame)
    entry_category_attributes.grid(row=4, column=1)
    # 使用新的参数列表调用 modify_category 方法
    tk.Button(frame, text="确认", command=lambda: ic.modify_category(type_combobox.get(), entry_new_category_name.get(), [attr.strip() for attr in entry_category_attributes.get().split() if attr.strip()])).grid(row=5, column=1, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(category_process_frame(root))).grid(row=6, column=1, columnspan=2)

    return frame
def show_category_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    # 显示所有类别
    tk.Button(frame, text="显示所有类别", command=ic.show_categories).grid(row=1, column=0, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(category_process_frame(root))).grid(row=2, column=0, columnspan=2)
    return frame


# GUI界面
def start_category_management():
    root = tk.Tk()
    root.title("类别管理系统")
    frame = category_process_frame(root)
    frame.tkraise()
    root.mainloop()

