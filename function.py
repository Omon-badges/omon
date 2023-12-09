users : list['Product'] = []
class Product:
    def __init__(self, id, name, price,term, count, join_at):
        self.id= id
        self.name = name
        self.price = price
        self.term = term
        self.count = count
        self.join_at = join_at

    def save(self):
        users.append(self)

    def delete(self):
        for i, user in enumerate(users):
            if user.id == self.id:
                del users[i]
print("\t\t\t\t\t\t\t\t\t\t\t\tDODA REGISTER BOTGA XUSH KELIBSIZ\t\t\t\t\t\t\t\t\t\t\n\n")
def main():
    n= int(input(
        "1.Produkta qo'shisht\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t2.Produktani o'chirish\n\n\n3.Produktalar list\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t4.Produktani yangilash\n\nMenyuni tanlang: "
    ))
    if n == 1:
        user = {
            "id": users[-1].id + 1 if users else 1,
            "name": input("Mahsulot nomi : "),
            "price": input("Mahsulot narxi : "),
            "term": input("Mahsulot yaroqliligi: "),
            "count": input("Mahsulot soni : "),
            "join_at": input("Mahsulot kelgan vaqt : ")
        }
        user_obj = Product(**user)
        user_obj.save()
        print("\n__________________________________________")
        print("|\t\t\t\tProdukta ro'yhatdan o'tkazildi✅\t\t\t\t")
        print("------------------------------------------\n")

        main()
    if n == 3:
        if not users:
            print("\n------------------------------------------")
            print("------Hozircha mahsulot mavjud emas ❌------")
            print("------------------------------------------\n")
            main()

        for user in users:
            print(user.__dict__)
        print("--------------------------------------------")
        main()
    if n == 2:
        id = int(input("Id :"))
        for i, user in enumerate(users):
            if user.id == id:
                del users[i]
        print("--------------------------------------------")
        main()
    if n == 4:
        id = int(input("id : "))
        for user in users:
            if user.id == id:
                find_user = user
                print(user.__dict__)
        fields = """
        1) Mahsulot nomi
        2) Mahsulot narxi
        3) Mahsulot yaroqliligi
        4) Mahsulot soni
        5) Mahsulot kelgan vaqt
        >>>"""
        key = input(fields)
        new_val = input("Yangi qiymatlarni bering : ")
        if key == "1":
            find_user.name = new_val
        if key == "2":
            find_user.price = new_val
        if key == "3":
            find_user.term = new_val
        if key == "4":
            find_user.join_at = new_val
        print("\n------------------------------------------")
        print("------------Produkta yangilandi ✅-----------")
        print("------------------------------------------\n")
        main()


main()
