from ADS1x15 import ADS1115
from time import sleep
from math import log

try:
	# Inicializo el ADS1115 en el bus I2C1 con direccion 0x48
	ads = ADS1115(1)
	# Mensaje de exito
	print("ADS1115 inicializado!")
	# Seteo ganancia
	ads.setGain(ads.PGA_4_096V)
	print("Ganancia seteada para leer hasta 4.096V")
	print("Procedo a leer NTC en AN1. Ctrl + C para salir...")
	print()
	# Canal para leer
	NTC_CH = 1
	# Resistencia en serie al NTC
	R = 10e3
	# Resistencia del NTC a 25 C
	R0 = 10e3
	# Valor de beta
	BETA = 3900

	while(True):
		# Leo el valor del canal AN1
		ntc_val = ads.readADC(NTC_CH)
		# Valor de tension del NTC
		ntc_v = ads.toVoltage(ntc_val)
		# Calculo valor de resistencia del NTC
		r_ntc = R / (3.3 / ntc_v - 1)
		# Calculo temperatura en C
		temp = (BETA * 298) / (298 * log(r_ntc / R0) + BETA) - 273
		# Imprimo valores
		print(f"Resistencia del NTC es {r_ntc:.2f}. La temperatura es de {temp:.2f}C")
		# Demora
		sleep(.5)

except Exception as e:
	# Algo salio mal
	print()
	print(e)
