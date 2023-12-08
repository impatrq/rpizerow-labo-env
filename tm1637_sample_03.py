from tm1637 import TM1637
from time import sleep
import requests
import json

# Inicializo el controlador
tm = TM1637(clk=12, dio=25)

# String para rotar
msg = "USD "

# Mensaje de indicacion
print("Aplicacion corriendo. Presione Ctrl + C para terminar")

try:
	# No hago nada en el bucle
	while True:
		# Muestro mensaje
		tm.show(msg)
		# Demora
		sleep(1)
		# Pido el valor del dolar
		dolar = requests.get("https://apiweb-ivancenyko.vercel.app/dolar-blue").json()["venta"]
		# Muestro el valor del dolar
		tm.number(dolar)
		# Demora
		sleep(2)

except KeyboardInterrupt:

	print()
	print("Aplicacion finalizada")
