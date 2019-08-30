salario_presidente=int(input("introduce salario presidente "))
print("salario presidente: " + str(salario_presidente))

salario_director=int(input("introduce salario dirctor "))
print("salario director: " + str(salario_director))

salario_jefe_area=int(input("introduce salario jefe area "))
print("salario jefe area: " + str(salario_jefe_area))

salario_administrativo=int(input("introduce salario administrativo "))
print("salario administrativo: " + str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("todo funcona correcta mente")
else:
	print("algo falla en esta empresa")