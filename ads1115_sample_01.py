from ADS1x15 import ADS1115
from time import sleep

try:
	# Inicializo el ADS1115 en el bus I2C1 con direccion 0x48
	ads = ADS1115(1)
	# Mensaje de exito
	print("ADS1115 inicializado!")
	# Seteo ganancia
	ads.setGain(ads.PGA_4_096V)
	print("Ganancia seteada para leer hasta 4.096V")
	print("Procedo a leer potenciometro en AN2. Ctrl + C para salir...")
	print()
	# Canal para leer
	POTE_CH = 2

	while(True):
		# Leo el valor del canal AN2
		pote_val = ads.readADC(POTE_CH)
		# Valor de tension del potenciometro
		pote_v = ads.toVoltage(pote_val)
		# Imprimo valores
		print(f"Valor analogico del pote en {pote_val}. El voltage equivale a {pote_v:.2f}V")
		# Demora
		sleep(.5)

except Exception as e:
	# Algo salio mal
	print()
	print(e)
