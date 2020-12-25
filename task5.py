
my_list = [7,5,3,2,2,1,6]
while True:
	print(f"Рейтинг натуральных чисел : {my_list}")
	a = int(input("Введите значение рейтинга : "))
	try:
		x = my_list.index(a)
		my_list.insert(x, a)
	except ValueError:
		print("Совпадений значения рейтинга нет")
		y_max = my_list.index(max(my_list))
		y_min = my_list.index(min(my_list))
		if a < my_list[y_min]:
			my_list.append(a)
		if a > my_list[y_max]:
			my_list.insert(y_max, a)
	print(f"Рейтинг натуральных чисел : {my_list}")





