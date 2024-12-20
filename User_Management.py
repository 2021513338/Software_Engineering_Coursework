import tkinter as tk
from tkinter import ttk
from User_Class import UserManagementSystem

ums = UserManagementSystem()

def switch_frame(frame):
    frame.tkraise()

def user_type_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="用户类型:").grid(row=0, column=0)
    tk.Button(frame, text="普通用户", command=lambda: switch_frame(next_frame(root, 'regular'))).grid(row=1, column=0, columnspan=2)
    tk.Button(frame, text="管理员", command=lambda: switch_frame(next_frame(root, 'admin'))).grid(row=2, column=0, columnspan=2)
    return frame

def next_frame(root, user_type):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="登录或注册:").grid(row=0, column=0)
    tk.Button(frame, text="注册", command=lambda: switch_frame(register_frame(root, user_type))).grid(row=1, column=0, columnspan=2)
    tk.Button(frame, text="登录", command=lambda: switch_frame(login_frame(root, user_type))).grid(row=2, column=0, columnspan=2)

    return frame

def login_frame(root, user_type):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    if user_type == 'regular':
        label_text = "普通用户登录"
        tk.Label(frame, text=label_text).grid(row=0, column=0, columnspan=2)

        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1, columnspan=2)
        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, columnspan=2)
        Button = tk.Button(frame, text="登录", command=lambda: ums.regular_login_or_register(username_entry.get(), password_entry.get()))
        Button.grid(row=3, column=0, columnspan=2)
        tk.Button(frame, text="返回", command=lambda: switch_frame(user_type_frame(root))).grid(row=4, column=0, columnspan=2)
    else:
        label_text = "管理员登录"
        tk.Label(frame, text=label_text).grid(row=0, column=0, columnspan=2)
        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1, columnspan=2)
        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, columnspan=2)
        Button = tk.Button(frame, text="登录", command=lambda: switch_frame(admin_next_frame(root)) if ums.handle_admin_login(username_entry.get(), password_entry.get()) else switch_frame(user_type_frame(root)))
        Button.grid(row=3, column=0, columnspan=2)
        tk.Button(frame, text="返回", command=lambda: switch_frame(user_type_frame(root))).grid(row=4, column=0, columnspan=2)
    return frame

def admin_next_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    tk.Label(frame, text="管理员操作选项:").grid(row=0, column=0)
    tk.Button(frame, text="审批普通用户", command=lambda: switch_frame(user_approve_frame(root))).grid(row=1, column=0, columnspan=2)
    tk.Button(frame, text="类别管理", command=lambda: ums.start_category_management()).grid(row=2, column=0, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(user_type_frame(root))).grid(row=4, column=0, columnspan=2)

    return frame

def register_frame(root, user_type):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")

    if user_type == 'regular':
        tk.Label(frame, text="普通用户注册:").grid(row=0, column=0)

        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1, columnspan=2)

        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, columnspan=2)

        tk.Label(frame, text="地址:").grid(row=3, column=0, sticky="e")
        address_entry = tk.Entry(frame)
        address_entry.grid(row=3, column=1, columnspan=2)

        tk.Label(frame, text="电话:").grid(row=4, column=0, sticky="e")
        contact_info_entry = tk.Entry(frame)
        contact_info_entry.grid(row=4, column=1, columnspan=2)

        tk.Label(frame, text="邮箱:").grid(row=5, column=0, sticky="e")
        email_entry = tk.Entry(frame)
        email_entry.grid(row=5, column=1, columnspan=2)

        tk.Button(frame, text="注册", command=lambda: ums.register_regular_user(username_entry.get(), address_entry.get(), contact_info_entry.get(), email_entry.get(), password_entry.get())).grid(row=6, column=0, columnspan=2)
    else:
        tk.Label(frame, text="管理员注册:").grid(row=0, column=0)
        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1, columnspan=2)

        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, columnspan=2)

        tk.Button(frame, text="注册", command=lambda: ums.register_admin_user(username_entry.get(), password_entry.get())).grid(row=3, column=0, columnspan=2)

    tk.Button(frame, text="返回", command=lambda: switch_frame(user_type_frame(root))).grid(row=7 if user_type == 'regular' else 4, column=0, columnspan=2)
    return frame

def user_approve_frame(root):
    frame = tk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew")
    tk.Label(frame, text="选择待审批用户:").grid(row=1, column=0)
    regular_users = [username for username, user in ums.users.items() if not user.is_approved]
    regular_combobox = ttk.Combobox(frame, values=regular_users)
    regular_combobox.grid(row=1, column=1, columnspan=2)
    tk.Button(frame, text="确认批准用户", command=lambda: ums.approve_user(regular_combobox.get())).grid(row=2, column=0, columnspan=2)
    tk.Button(frame, text="返回", command=lambda: switch_frame(user_type_frame(root))).grid(row=3, column=0, columnspan=2)
    return frame

def start_user_management():
    root = tk.Tk()
    root.title("用户管理系统")
    frame = user_type_frame(root)
    frame.tkraise()
    root.mainloop()








