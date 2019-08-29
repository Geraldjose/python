edad=int(input("introduce tu edad por favor: "))

while edad<5 or edad>100:
	print("has introducido una edad incorrecta. vuelve a intentarlo")
	edad=int(input("introduce tu edad por favor: "))

print("gracias por colaborar. puedes pasar")
print("edad del aspirante " + str(edad))