# Raspberry Pi Zero W Labo Environment

## Instrucciones

1- Si no lo hemos hecho ya, hacer un [fork](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) de este repositorio para que tengamos una copia bajo nuestro usuario.

2- Asegurarse de que la computadora desde donde se van a conectar esté en la **Red Alumnos**.

3- Iniciar sesion en la RPiZeroW con SSH a traves de Putty o shell. El usuario y clave son `rpizerow`. En cuanto al hostname, vamos a acceder con rpizerow-0x.local donde x es el numero de la RPiZeroW que queremos usar. 

Ejemplo para SSH desde shell:

```bash
ssh rpizerow@rpizerow-01.local
```

Si usan Putty, solo hace falta escribir en el campo Host Name:

```
rpizerow@rpizerow-01.local
```

Con esto nos logueamos con el usuario rpizerow en la RPiZeroW 01.

4- Crear dentro del home de rpizerow un directorio con nuestro apellido con el comando _mkdir_ y luego entrar al mismo. Ejemplo:

```bash
mkdir gonzalez && cd gonzalez
```

5- Clonar el fork de este repositorio con el comando a continuación reemplazando _USERNAME_ por el que corresponda.:

```bash
git clone https://github.com/USERNAME/rpizerow-labo-env.git
```

**Nota: si les pide autorización de usuario y contraseña de GitHub, el link al repositorio lo copiaron mal.**

6- Navegar hasta el repositorio con _cd_ y crear un entorno virtual. Sería:

```bash
cd rpizerow-labo-env && python -m venv .rpizerow-env
```

Este comando en particular toma un tiempo en resolverse.

7- Activar el entorno virtual e instalar los requisitos:

```bash
source .rpizerow-env/bin/activate && python -m pip install -r requirements.txt
```

8- Ir hasta el directorio del ejercicio a resolver. Ejemplo, si quisiera resolver el ejercicio 3 de Python haría:

```bash
cd actividades_python/ej_03
```

9- Resolver el ejercicio propuesto dentro del directorio correspondiente usando el editor `nano` para escribir el código. Para abrir nano (ya estando en el directorio que corresponda) y crear un archivo pueden escribir:

```bash
nano FILENAME
```

Reemplazando _FILENAME_ por el nombre del archivo apropiado. Pueden encontrar informacion sobre los comandos basicos de nano en este [link](https://www.cheatsheet.wtf/Nano/).

10- Happy coding!

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
