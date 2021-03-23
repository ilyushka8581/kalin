def start():
	password = input("Enter password: ")

	if password == "1":
		name = input("Your name: ")
		print("Добро пожаловать", name)
		print("Я, Калин, ваш помощник. Буду рада вам помочь")
		print("Для окончания разговора нажмите Ctrl+C")

		name_assistent = "Калин:"

		def hello():
			if message == "Привет":
				print(name_assistent, "Привет")
			else:
				if message == "привет":
					print(name_assistent, "Привет")
				else:
					pass
				
		def how_are_you():
			if message == "Как дела?":
				print(name_assistent, "Хорошо, у тебя как?")
				input()
				print(name_assistent, "Понятно")
			else:
				if message == "как дела?":
					print(name_assistent, "Хорошо, у тебя как?")
					input()
					print(name_assistent, "Понятно")
				else:
					if message == "Как дела":
						print(name_assistent, "Хорошо, у тебя как?")
						input()
						print(name_assistent, "Понятно")
					else:
						if message == "как дела":
							print(name_assistent, "Хорошо, у тебя как?")
							input()
							print(name_assistent, "Понятно")
						else:
							pass

		def praise():
			if message == "молодец":
				print(name_assistent, "Спасибо")
			else:
				if message == "Молодец":
					print(name_assistent, "Спасибо")

		def chto_delaesh():
			if message == "Что делаешь?":
				print("Вычисляю уравнения, ты что делаешь?")
				input()
				print("Удачи")
			else:
				if message == "что делаешь?":
					print("Вычисляю уравнения, ты что делаешь?")
					input()
					print("Тебе, наверное, очень интересно")
				else:
					if message == "Что делаешь":
						print("Вычисляю уравнения, ты что делаешь?")
						input()
						print("Классно")
					else:
						if message == "что делаешь":
							print("Вычисляю уравнения, ты что делаешь?")
							input()
							print("Понятно, ты человек, ты можешь, а я просто робот и не могу это делать")
						else:
							pass

		def calculator():
			if message == "Посчитай, пожалуйста":
				print("Я могу считать только по 2 числа")
				num1 = int(input("Введите первое число: "))
				num2 = int(input("Введите второе число: "))
				oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
				if oper == "умножение":
					print("Получилось:", num1 * num2)
				else:
					if oper == "сложение":
						print("Получилось:", num1 + num2)
					else:
						if oper == "вычитание":
							print("Получилось:", num1 - num2)
						else:
							if oper == "деление":
								print("Получилось:", num1 / num2)
							else:pass
			else:
				if message == "посчитай, пожалуйста":
					print("Я могу считать только по 2 числа")
					num1 = int(input("Введите первое число: "))
					num2 = int(input("Введите второе число: "))
					oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
					if oper == "умножение":
						print("Получилось:", num1 * num2)
					else:
						if oper == "сложение":
							print("Получилось:", num1 + num2)
						else:
							if oper == "вычитание":
								print("Получилось:", num1 - num2)
							else:
								if oper == "деление":
									print("Получилось:", num1 / num2)
								else:pass
				else:
					if message == "Посчитай":
						print("Я могу считать только по 2 числа")
						num1 = int(input("Введите первое число: "))
						num2 = int(input("Введите второе число: "))
						oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
						if oper == "умножение":
							print("Получилось:", num1 * num2)
						else:
							if oper == "сложение":
								print("Получилось:", num1 + num2)
							else:
								if oper == "вычитание":
									print("Получилось:", num1 - num2)
								else:
									if oper == "деление":
										print("Получилось:", num1 / num2)
									else:pass
					else:
						if message == "посчитай":
							print("Я могу считать только по 2 числа")
							num1 = int(input("Введите первое число: "))
							num2 = int(input("Введите второе число: "))
							oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
							if oper == "умножение":
								print("Получилось:", num1 * num2)
							else:
								if oper == "сложение":
									print("Получилось:", num1 + num2)
								else:
									if oper == "вычитание":
										print("Получилось:", num1 - num2)
									else:
										if oper == "деление":
											print("Получилось:", num1 / num2)
										else:pass
						else:
							if message == "Калькулятор, пожалуйста":
								print("Я могу считать только по 2 числа")
								num1 = int(input("Введите первое число: "))
								num2 = int(input("Введите второе число: "))
								oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
								if oper == "умножение":
									print("Получилось:", num1 * num2)
								else:
									if oper == "сложение":
										print("Получилось:", num1 + num2)
									else:
										if oper == "вычитание":
											print("Получилось:", num1 - num2)
										else:
											if oper == "деление":
												print("Получилось:", num1 / num2)
											else:pass
							else:
								if message == "калькулятор, пожалуйста":
									print("Я могу считать только по 2 числа")
									num1 = int(input("Введите первое число: "))
									num2 = int(input("Введите второе число: "))
									oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
									if oper == "умножение":
										print("Получилось:", num1 * num2)
									else:
										if oper == "сложение":
											print("Получилось:", num1 + num2)
										else:
											if oper == "вычитание":
												print("Получилось:", num1 - num2)
											else:
												if oper == "деление":
													print("Получилось:", num1 / num2)
												else:pass
								else:
									if message == "Калькулятор":
										print("Я могу считать только по 2 числа")
										num1 = int(input("Введите первое число: "))
										num2 = int(input("Введите второе число: "))
										oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
										if oper == "умножение":
											print("Получилось:", num1 * num2)
										else:
											if oper == "сложение":
												print("Получилось:", num1 + num2)
											else:
												if oper == "вычитание":
													print("Получилось:", num1 - num2)
												else:
													if oper == "деление":
														print("Получилось:", num1 / num2)
													else:pass
									else:
										if message == "калькулятор":
											print("Я могу считать только по 2 числа")
											num1 = int(input("Введите первое число: "))
											num2 = int(input("Введите второе число: "))
											oper = input("Что хотите сделать с этими числами(пишите с маленькой буквы, например, умножение): ")
											if oper == "умножение":
												print("Получилось:", num1 * num2)
											else:
												if oper == "сложение":
													print("Получилось:", num1 + num2)
												else:
													if oper == "вычитание":
														print("Получилось:", num1 - num2)
													else:
														if oper == "деление":
															print("Получилось:", num1 / num2)
														else:pass
										else:
											pass

		def stop_stop():
			if message == "Стоп":
				stop()
			else:
				if message == "стоп":
					stop()
				else:
					pass

		while True:
			message = input("Пишите: ")
			hello()
			how_are_you()
			praise()
			chto_delaesh()
			calculator()
			stop_stop()

def stop():
	exit()

try:
	start()
except KeyboardInterrupt:
	stop()