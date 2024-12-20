import json
from tkinter import messagebox

class Category:
    def __init__(self, name, attributes=None):
        self.name = name
        self.attributes = attributes if attributes is not None else []

    def add_attribute(self, attr_name):
        if attr_name not in self.attributes:
            self.attributes.append(attr_name)

    def get_attributes(self):
        return self.attributes


class ItemCategory:
    _instance = None

    def __new__(cls, filename='Category/categories.json'):
        if cls._instance is None:
            cls._instance = super(ItemCategory, cls).__new__(cls)
            cls._instance.categories = {}  # 用于存储所有类别的字典
            cls._instance.filename = filename
            cls._instance.load_category()
        return cls._instance

    def save_category(self):
        categories_data = []
        for category_name, category in self.categories.items():
            categories_data.append({
                'name': category.name,
                'attributes': category.get_attributes()
            })
        with open(self.filename, 'w') as f:
            json.dump(categories_data, f, indent=4)

    def load_category(self):
        self.categories = {}  # 重置类别存储
        try:
            with open(self.filename, 'r') as f:
                categories_data = json.load(f)
                for category_data in categories_data:
                    category = Category(category_data['name'], category_data['attributes'])
                    self.categories[category.name] = category
        except FileNotFoundError:
            messagebox.showerror("Error", "Category file not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Invalid JSON format in category file.")

    def add_category(self, name, attributes):
        # 检查是否已经存在同名的类别
        if name in self.categories:
            messagebox.showerror("Error", f"类别 '{name}' 已经存在。")
        else:
            new_category = Category(name, attributes)
            self.categories[name] = new_category
            self.save_category()
            messagebox.showinfo("Success", f"类别 '{name}' 添加成功。")

    def modify_category(self, current_category_name, new_category_name, new_attributes):
        # 修改一个类别的名称和属性
        if current_category_name in self.categories:
            if new_category_name in self.categories:
                messagebox.showerror("Error", f"类别 '{new_category_name}' 已经存在。")
            else:
                category = self.categories[current_category_name]
                # 更新类别名称
                category.name = new_category_name
                self.categories[new_category_name] = category
                del self.categories[current_category_name]

                # 用新的属性列表完全替换旧的属性
                category.attributes = list(new_attributes)
                self.save_category()
                messagebox.showinfo("Success", f"类别 '{new_category_name}' 已被成功更新。")
        else:
            messagebox.showerror("Error", f"类别 '{current_category_name}' 未找到。")


    def show_categories(self):
        # 显示所有类别
        msg = "Categories:\n"
        for category_name, category in self.categories.items():
            msg += f"Category: {category_name}, Attributes: {category.get_attributes()}\n"
        messagebox.showinfo("Categories", msg)

    def get_all_categories(self):
        # 获取所有类别
        return list(self.categories.values())