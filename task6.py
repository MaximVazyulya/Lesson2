#(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
#(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})

prodact_list = []
prodact_dict = {}
keys_list = ["название", "цена", "кол-во", "ед"]
i = 0
j = 0
while True:
    num = int(input ("Введите номер товара : "))
    prodact_list.append(num)
    for k in keys_list:
        prodact_dict[k] = input(f"Введите {k} товара : ")
        print(prodact_dict)
    prodact_list.append(prodact_dict)
    z = int(input("ЕщЁ 1-продолжить ввод, 0-закончить ввод : "))
    print(z)
    if z == 0:
        break
    i += 1
print(prodact_list)
print(type(prodact_list))
b = tuple(prodact_list)
print(b)
print(type(b))



