import json
import re
from tkinter import messagebox
from Category_Class import ItemCategory  # 导入ItemCategory单例

class Item:
    def __init__(self, name, description, location, contact_phone, email, category, keys=None):
        self.name = name
        self.description = description
        self.location = location
        self.contact_phone = contact_phone
        self.email = email
        self.category = category
        self.keys = keys if keys is not None else []

    def add_key(self, key):
        self.keys.append(key)

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Location: {self.location}\n"
                f"Contact Phone: {self.contact_phone}\n"
                f"Email: {self.email}\n"
                f"Category: {self.category.name}\n"
                f"Keys: {self.keys}")

class ItemBook:
    def __init__(self, item_filename='Item/items.json', category_filename='Category/categories.json'):
        self.items = []
        self.size = 0
        self.category_manager = ItemCategory()  # 使用ItemCategory单例
        self.categories = self.category_manager.categories  # 直接引用ItemCategory中的categories属性
        self.item_filename = item_filename
        self.category_filename = category_filename
        self.load_items()

    def save_items(self):
        items_data = [{'name': item.name, 'description': item.description, 'location': item.location,
                      'contact_phone': item.contact_phone, 'email': item.email, 'category': item.category.name,
                      'keys': item.keys} for item in self.items]
        with open(self.item_filename, 'w') as f:
            json.dump(items_data, f, indent=4)

    def load_items(self):
        try:
            with open(self.item_filename, 'r', encoding='utf-8') as f:  # 确保使用utf-8编码读取文件
                items_data = json.load(f)
                for item_data in items_data:
                    category = self.categories.get(item_data['category'])
                    if not category:
                        messagebox.showerror("Error", "Specified item category not found.")
                        continue  # 如果类别不存在，则跳过当前项

                    item = Item(
                        name=item_data['name'],
                        description=item_data['description'],
                        location=item_data['location'],
                        contact_phone=item_data['contact_phone'],
                        email=item_data['email'],
                        category=category,  # 使用Category实例
                        keys=item_data.get('keys', [])  # 使用get方法以避免keys字段缺失的错误
                    )
                    self.items.append(item)
                    self.size += 1  # 更新物品数量
        except FileNotFoundError:
            messagebox.showerror("Error", "Items file not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Items file is not a valid JSON.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def load_attributes(self):
        # 返回所有类别的属性列表
        attributes_list = {}
        for category_name, category in self.categories.items():
            attributes_list[category_name] = category.get_attributes()
        return attributes_list

    def add_item(self, name, description, location, contact_phone, email, category_name, keys=None):
        for item in self.items:
            if item.name == name and item.category.name == category_name:
                messagebox.showerror("Error", "物品已经存在，无需重复录入。")
                return

        category = self.categories.get(category_name)
        if not category:
            messagebox.showerror("Error", "Specified item category not found.")
            return

        item = Item(name, description, location, contact_phone, email, category, keys)
        self.items.append(item)
        self.save_items()
        messagebox.showinfo("Success", "物品添加成功。")

    def delete_item(self, name, category_name):
        for i, item in enumerate(self.items):
            if item.name == name and item.category.name == category_name:
                self.items.pop(i)
                messagebox.showinfo("Success", "删除完毕。")
                return
        messagebox.showerror("Error", "抱歉！您想删除的物品不存在。")

    def show_item(self):
        if not self.items:
            messagebox.showinfo("Info", "物品清单为空！")
            return
        for item in self.items:
            messagebox.showinfo("Info", str(item))

    def find_item(self, name, keyword, category_name):
        found = False
        for item in self.items:
            # 使用正则表达式查找“用户名：”后的用户名
            user_name_match = re.search(r"用户名：(.+)", item.description)
            if user_name_match:
                user_name = user_name_match.group(1)
            else:
                user_name = ""

            if item.name == name and item.category.name == category_name:
                if user_name == keyword or keyword in item.description:
                    messagebox.showinfo("Found", str(item))
                    found = True
                    break  # 找到匹配项后退出循环
        if not found:
            messagebox.showerror("Error", "抱歉！您想查找的物品不存在。")