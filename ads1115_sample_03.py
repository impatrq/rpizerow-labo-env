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
	print("Procedo a leer LDR en AN0. Ctrl + C para salir...")
	print()
	# Canal para leer
	LDR_CH = 0

	while(True):
		# Leo el valor del canal AN0
		ldr_val = ads.readADC(LDR_CH)
		# Valor de voltage del LDR (en realidad calculo de la resistencia porque leo sobre el LDR)
		ldr_v = 3.3 - ads.toVoltage(ldr_val)
		# Porcentaje de luz (3.3V es 100%)
		ldr_per = ldr_v * 100 / 3.3
		# Imprimo valores
		print(f"Valor analogico del LDR es {ldr_val}. El porcentaje de luz equivale a {ldr_per:.2f}%")
		# Demora
		sleep(.5)

except Exception as e:
	# Algo salio mal
	print()
	print(e)
