def check_password(content):
 	if content == "123123":
 		print("Welcome")
 	else:
 		print("error")

password = input("Enter password: ")
check_password(password)