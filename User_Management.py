import tkinter as tk
from tkinter import messagebox
from Item_Management import ItemBook, start_item_management, start_category_management

class User:
    def __init__(self, username, address, contact_info, email, password, is_approved=False):
        self.username = username
        self.address = address
        self.contact_info = contact_info
        self.email = email
        self.password = password
        self.is_approved = is_approved

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, '', '', '', password, False)
        self.item_types = {}

class RegularUser(User):
    def __init__(self, username, address, contact_info, email, password):
        super().__init__(username, address, contact_info, email, password)

class UserManagementSystem:
    def __init__(self):
        self.users = {}
        self.admins = {}

    def register_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user
            return True
        return False

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return user
        return None

    def add_admin(self, username, password):
        if username not in self.admins:
            self.admins[username] = Admin(username, password)
            return True
        return False

    def admin_login(self, username, password):
        admin = self.admins.get(username)
        if admin and admin.password == password:
            return admin
        return None

ums = UserManagementSystem()
ib = ItemBook()

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

    label_text = "普通用户登录" if user_type == 'regular' else "管理员登录"
    tk.Label(frame, text=label_text).grid(row=0, column=0, columnspan=2)

    tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e")
    username_entry = tk.Entry(frame)
    username_entry.grid(row=1, column=1, columnspan=2)
    tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e")
    password_entry = tk.Entry(frame, show="*")
    password_entry.grid(row=2, column=1, columnspan=2)

    tk.Button(frame, text="登录", command=lambda: (regular_login_or_register if user_type == 'regular' else admin_login)(username_entry.get(), password_entry.get())).grid(row=3, column=0, columnspan=2)
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

        tk.Button(frame, text="注册", command=lambda: register_regular_user(
            username_entry.get(),
            address_entry.get(),
            contact_info_entry.get(),
            email_entry.get(),
            password_entry.get()
        )).grid(row=6, column=0, columnspan=2)
    else:
        tk.Label(frame, text="管理员注册:").grid(row=0, column=0)
        tk.Label(frame, text="用户名:").grid(row=1, column=0, sticky="e")
        username_entry = tk.Entry(frame)
        username_entry.grid(row=1, column=1, columnspan=2)

        tk.Label(frame, text="密码:").grid(row=2, column=0, sticky="e")
        password_entry = tk.Entry(frame, show="*")
        password_entry.grid(row=2, column=1, columnspan=2)

        tk.Button(frame, text="注册", command=lambda: register_admin_user(
            username_entry.get(),
            password_entry.get()
        )).grid(row=3, column=0, columnspan=2)

    tk.Button(frame, text="返回", command=lambda: switch_frame(user_type_frame(root))).grid(
        row=7 if user_type == 'regular' else 4, column=0, columnspan=2)
    return frame

def register_admin_user(username, password):
    if ums.add_admin(username, password):
        messagebox.showinfo("Success", "管理员注册成功。")
    else:
        messagebox.showerror("Error", "管理员已存在。")

def register_regular_user(username, address, contact_info, email, password):
    if ums.register_user(RegularUser(username, address, contact_info, email, password)):
        messagebox.showinfo("Success", "普通用户注册成功。")
    else:
        messagebox.showerror("Error", "普通用户已存在。")

def regular_login_or_register(username, password):
    user = ums.login_user(username, password)
    if user:
        messagebox.showinfo("Success", "普通用户登录成功。")
        user.is_approved = True
        start_item_management_system(user)
    else:
        messagebox.showerror("Error", "普通用户登录失败。")

def admin_login(username, password):
    admin = ums.admin_login(username, password)
    if admin:
        messagebox.showinfo("Success", "管理员登录成功。")
        admin.is_approved = True
        start_category_management_system(admin)
    else:
        messagebox.showerror("Error", "管理员登录失败。")

def start_item_management_system(user):
    if user and user.is_approved:
        start_item_management()  # 启动物品管理系统
    else:
        messagebox.showerror("Error", "用户未认证，无法访问物品管理系统。")

def start_category_management_system(admin):
    if admin and admin.is_approved:
        start_category_management()  # 启动物品管理系统
    else:
        messagebox.showerror("Error", "用户未认证，无法访问物品管理系统。")

def start_user_management():
    root = tk.Tk()
    root.title("用户管理系统")

    frame = user_type_frame(root)
    frame.tkraise()

    root.mainloop()






