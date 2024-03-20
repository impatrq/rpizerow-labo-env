# Raspberry Pi Zero W Labo Environment

## Instrucciones

1- Si no lo hemos hecho ya, hacer un fork de este repositorio para que tengamos una copia bajo nuestro usuario.

2- Iniciar sesion en la RPiZeroW con SSH a traves de Putty o shell. El usuario y clave son `rpizerow`. En cuanto al hostname, vamos a acceder con rpizerow-0x.local donde x es el numero de la RPiZeroW que queremos usar. Ejemplo para SSH desde shell:

```bash
ssh rpizerow@rpizerow-01.local
```

Con esto nos logueamos con el usuario rpizerow en la RPiZeroW 01. **La computadora o dispositivo desde donde se conecten tiene que estar conectada a Red Alumnos**.

3- Crear dentro del home de rpizerow un directorio con nuestro apellido con el comando _mkdir_.

4- Entrar al directorio personal con el comando _cd_ y clonar el fork de este repositorio como:

```bash
git clone https://github.com/USERNAME/rpizerow-labo-env.git
```

Reemplazando _USERNAME_ por el que corresponda.

5- Navegar hasta el repositorio con _cd_ y crear un entorno virtual con:

```bash
python -m venv .rpizerow-env
```

Este comando en particular toma un tiempo en resolverse.

6- Activar el entorno virtual e instalar los requisitos:

```bash
source .rpizerow-env/bin/activate && python -m pip install -r requirements.txt
```

7- Resolver los ejercicios propuestos dentro del directorio correspondiente usando el editor `nano`. Para abrir nano y crear un archivo pueden escribir:

```bash
nano FILENAME
```

Reemplazando _FILENAME_ por el nombre del archivo apropiado. Pueden encontrar informacion sobre los comandos basicos de nano en este [link](https://www.cheatsheet.wtf/Nano/).

8- Happy coding!

## GitHub CLI

Vamos a usar GitHub CLI como herramienta para poder autorizar las credenciales cuando intentemos pushear. Instrucciones de como usarlo pueden encontrarlas [aqui](github_cli.md).

## Documentacion sobre placa de desarrollo

En la medida que se desarrollen las distintas actividades, va a ser necesario informacion del hardware que estamos usando. Pueden encontrar esquematico, PCB y otros documentos en este [repositorio](https://github.com/impatrq/rpizerow-labo-kit).

## Documentacion sobre modulos de Python

Las bibliotecas de Python de las que vamos a hacer uso pueden encontrarse en el [requirements.txt](requirements.txt). Aqui dejamos links a la documentacion o repositorio de cada una de las bibliotecas:

- [gpiozero](https://pypi.org/project/gpiozero/) para perifericos de la RPiZeroW
- [raspberrypi-tm1637](https://pypi.org/project/raspberrypi-tm1637/) para controlar el display 7 segmentos
- [ADS1x15-ADC](https://github.com/chandrawi/ADS1x15-ADC) para usar el ADC externo
- [Adafruit-BMP](https://github.com/adafruit/Adafruit_Python_BMP) para usar el BMP180
- [requests](https://pypi.org/project/requests/) para hacer consultas por HTTP
