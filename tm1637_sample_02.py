from tm1637 import TM1637
from time import sleep

# Inicializo el controlador
tm = TM1637(clk=12, dio=25)

# String para rotar
msg = "   HELP"

# Mensaje de indicacion
print("Aplicacion corriendo. Presione Ctrl + C para terminar")

try:
	# No hago nada en el bucle
	while True:
		# Muestro mensaje (primeros 4 caracteres)
		tm.show(msg[:4])
		# Roto string
		msg = msg[1:] + msg[0]
		# Demora
		sleep(1)

except KeyboardInterrupt:

	print()
	print("Aplicacion finalizada")
