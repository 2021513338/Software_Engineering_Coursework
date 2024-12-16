# main.py
import tkinter as tk
from User_Management import start_user_management

def main():
    # 初始化Tkinter的主窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 启动用户管理系统界面
    start_user_management()

if __name__ == "__main__":
    main()