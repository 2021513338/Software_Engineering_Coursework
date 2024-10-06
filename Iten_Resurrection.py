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
        if self.size >= 1000:
            print("物品清单已达最大容量，请删除部分物品后，再继续添加。")
            return
        name = input("请输入物品名称：")
        owner = input("请输入主人名称：")
        phone_num = input("请输入联系方式：")

        for item in self.items:
            if item.name == name and item.owner == owner:
                print("物品已经存在，无需重复录入。")
                return

        self.items.append(Item(name, owner, phone_num))
        self.size += 1
        print("添加完毕。")

    def delete_item(self):
        if self.size == 0:
            print("物品清单为空！不可再进行删除。")
            return

        name = input("请输入要删除的物品：")
        owner = input("请输入物品主人的名字：")

        for i, item in enumerate(self.items):
            if item.name == name and item.owner == owner:
                self.items.pop(i)
                self.size -= 1
                print("删除完毕。")
                return

        print("抱歉！您想删除的物品不存在。")

    def show_item(self):
        if self.size == 0:
            print("物品清单为空！")
            return

        print(f"{'物品名称':<15}{'主人名称':<15}{'联系方式'}")
        for item in self.items:
            print(f"{item.name:<15}{item.owner:<15}{item.phone_num}")

    def find_item(self):
        name = input("请输入您想要查找的物品名：")
        found = False
        for item in self.items:
            if item.name == name:
                print(f"{'物品名称':<15}{'主人名称':<15}{'联系方式'}")
                print(f"{item.name:<15}{item.owner:<15}{item.phone_num}")
                found = True
        if not found:
            print("抱歉！您想查找的物品不存在。")

def main():
    ib = ItemBook()

    while True:
        print("欢迎使用物品交换系统！以下是本系统的功能：")
        print("1.添加物品 2.删除物品 3.显示物品 4.查找物品 0.退出")
        choice = input("请输入您的选择：")

        if choice == "1":
            ib.add_item()
        elif choice == "2":
            ib.delete_item()
        elif choice == "3":
            ib.show_item()
        elif choice == "4":
            ib.find_item()
        elif choice == "0":
            print("欢迎下次使用！")
            break
        else:
            print("抱歉，请输入0-4之间的阿拉伯数字。")

if __name__ == "__main__":
    main()