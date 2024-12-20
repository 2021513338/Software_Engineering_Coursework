import json
from tkinter import messagebox
from Item_Management import start_item_management
from Category_Management import start_category_management
class User:
    def __init__(self, username, address, contact_info, email, password, is_approved=False):
        self.username = username
        self.address = address
        self.contact_info = contact_info
        self.email = email
        self.password = password
        self.is_approved = is_approved

class Admin(User):
    def __init__(self, username, password, address='', contact_info='', email='', is_approved=False):
        super().__init__(username, address, contact_info, email, password, is_approved)

class RegularUser(User):
    def __init__(self, username, address, contact_info, email, password):
        super().__init__(username, address, contact_info, email, password)

class UserManagementSystem:
    def __init__(self, filename='User/users.json'):
        self.users = {}
        self.admins = {}
        self.filename = filename
        self.load_users()

    def save_users(self):
        try:
            users_data = {'users': {k: v.__dict__ for k, v in self.users.items()},
                          'admins': {k: v.__dict__ for k, v in self.admins.items()}}
            with open(self.filename, 'w') as f:
                json.dump(users_data, f, indent=4)
        except Exception as e:
            print(f"保存用户信息时出错：{e}")

    def load_users(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.users = {k: RegularUser(**v) if 'is_approved' not in v else Admin(**v) for k, v in
                              data.get('users', {}).items()}
                self.admins = {k: Admin(**v) for k, v in data.get('admins', {}).items()}
        except FileNotFoundError:
            print(f"文件 {self.filename} 未找到。初始化为空用户和管理员字典。")
            self.users = {}
            self.admins = {}
        except json.JSONDecodeError as e:
            print(f"解析JSON时出错：{e}。初始化为空用户和管理员字典。")
            self.users = {}
            self.admins = {}
        except Exception as e:
            print(f"加载用户信息时出错：{e}")

    def register_user(self, user):
        if user.username not in self.users:
            self.users[user.username] = user
            self.save_users()
            return True
        else:
            return False

    def login_user(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            return True
        else:
            return False

    def add_admin(self, username, password):
        if username not in self.admins:
            self.admins[username] = Admin(username, password)
            self.save_users()
            return True
        else:
            return False

    def admin_login(self, username, password):
        admin = self.admins.get(username)
        if admin and admin.password == password:
            return True
        else:
            return False

    def approve_user(self, username):
        user = self.users.get(username)
        if user and not user.is_approved:
            user.is_approved = True
            self.save_users()
            messagebox.showinfo("Success", f"普通用户{username}批准成功。")
            return True
        else:
            return False

    def register_admin_user(self, username, password):
        if self.add_admin(username, password):
            messagebox.showinfo("Success", "管理员注册成功。")
        else:
            messagebox.showerror("Error", "管理员已存在。")

    def register_regular_user(self, username, address, contact_info, email, password):
        if self.register_user(RegularUser(username, address, contact_info, email, password)):
            messagebox.showinfo("Success", "普通用户注册成功，待批准。")
        else:
            messagebox.showerror("Error", "普通用户已存在。")

    def regular_login_or_register(self, username, password):
        result = self.login_user(username, password)
        if result:
            user = self.users.get(username)
            if user.is_approved:
                messagebox.showinfo("Success", "普通用户登录成功。")
                start_item_management()
            else:
                messagebox.showinfo("Success", "普通用户待批准。")
        else:
            messagebox.showerror("Error", "普通用户登录失败。")

    def handle_admin_login(self, username, password):
        result = self.admin_login(username, password)
        if result:
            messagebox.showinfo("Success", "管理员登录成功。")
            return True
        else:
            messagebox.showerror("Error", "管理员登录失败。")
            return False

    def start_category_management(self):
        messagebox.showinfo("Info", "启动类别管理系统。")
        start_category_management()

