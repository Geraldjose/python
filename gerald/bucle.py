valido=False
email= str(input("intruduce tu email: "))

print(len(email))

print(range(5))

for i in range(len(email)):
	if email[i] == "@":
		valido=True

if valido:
	print("email correcto")
else:
	print("email incorrecto")
