from Adafruit_BMP import BMP085
from time import sleep

# Mensaje de bienvenida
print("Lectura de tempera y presion con BMP180. Ctrl + C para terminar")
print()

try:
	# Intento encontrar e inicializar el sensor con resolucion mas alta
	bmp = BMP085.BMP085(mode=BMP085.BMP085_ULTRAHIGHRES)

	while True:
		# Leo temperatura
		temp = bmp.read_temperature()
		# Leo presion
		pres = bmp.read_pressure()
		# Muestro valores
		print(f"Temperatura es de {temp:.2f} C y la presion es de {pres:.2f} Pa")
		# Demora
		sleep(.5)

except KeyboardInterrupt:
	# Termino el programa
	print()
	print("Programa finalizado")

except:
	# Algo salio mal con el sensor
	print("Error con el sensor")

