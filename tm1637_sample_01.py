from tm1637 import TM1637

# Inicializo el controlador
tm = TM1637(clk=12, dio=25)

# Muestro mensaje
tm.show("HELP")

# Mensaje de indicacion
print("Aplicacion corriendo. Presione Ctrl + C para terminar")

try:
	# No hago nada en el bucle
	while True:
		pass

except KeyboardInterrupt:

	print()
	print("Aplicacion finalizada")
