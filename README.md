# Raspberry Pi Zero W Labo Environment

Contenidos del README:

- [Como empezar](#como-empezar)
- [git add, commit, push](#git-add-commit-y-push)
- [GitHub CLI](#github-cli)
- [Documentación sobre placa de desarrollo](#documentación-sobre-placa-de-desarrollo)
- [Documentación sobre modulos de Python](#documentación-sobre-modulos-de-python)

## Como empezar

1- Si no lo hemos hecho ya, hacer un [fork](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) de este repositorio para que tengamos una copia bajo nuestro usuario. Si ya hicimos un fork previamente, asegurémonos de que el fork esté [sincronizado](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) con el respositorio original. 

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

## git add, commit y push

Una vez que hayamos terminado una actividad o ejercicio, tenemos que hacer los cambios en el repositorio con git para poder sincronizarlos. La lógica siempre es `git add`, `git commit`, `git push`.

Cuando tenemos algún archivo nuevo o modificado, lo primero es agregarlo a git para que trackee los cambios:

```bash
git add ruta_y_nombre_de_archivo
```

Luego, vamos a tener que especificar quién somos para que quede registrado la persona que está haciendo los cambios en el repositorio con `git config`. Ejemplo:

```bash
git config user.email "gonzalez@impatrq.com" && git config user.name "Gonzalo Gonzalez"
```

Después, tenemos que hacer un commit para registrar el cambio que hicimos y proporcionar un mensaje apropiado con el tipo de cambio según el estándar de [commits convencionales](https://github.com/angular/angular/blob/22b96b9/CONTRIBUTING.md#-commit-message-guidelines). Ejemplo:

```bash
git commit -m "feat: programa que prende un LED rojo con boton"
```

Cuando hayamos hecho todos los commits, vamos a seguir las instrucciones de la sección [GitHub CLI](#github-cli) para poder autorizar a la RPiZeroW para pushar a nuestro repositorio y luego hacer el push usando:

```bash
git push
```

## GitHub CLI

Estas son algunas instrucciones para poder pushear a un repo personal desde la RPiZeroW.

Vamos a usar [GitHub CLI](https://cli.github.com/) para facilitar el problema de la autenticacion de credenciales. Este programa ya esta instalado en todas las placas de desarrollo, puede verificarse escribiendo:

``` bash
gh --version
```

Y debemos ver que no hay error en cuanto al comando.

Para poder usarlo, vamos a necesitar crear un token de acceso personal en GitHub para que al pushear nuestros cambios a un repositorio personal, GitHub pueda acreditar nuestra identidad. Esto puede hacerse desde la configuracion en nuestro perfil de GitHub, dentro de la seccion de configuracion de desarrollador. Informacion mas detallada pueden encontrarla en este [link](https://docs.github.com/en/enterprise-server@3.9/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Al crear el token, tendremos que darle ciertos alcances. GitHub CLI nos va a pedir que los alcances minimos sean: `repo`, `read:org` y `workflow`.

Para poder usar GitHub CLI escribimos en el bash:

```bash
gh auth login
```

Esto nos va a solicitar algunos datos:

- A que tipo de cuenta loguearse? GitHub.com
- Protocolo preferido? HTTPS
- Autenticar Git con credenciales de GitHub? Si
- Como autenticar GitHub CLI? Con token, vamos a pegar el que generamos cuando lo solicite.

Una vez logueados, vamos a poder pushear nuestros cambios a repositorios personales sin inconvenientes. Cuando estemos listos para salir de la RPiZeroW, vamos a desloguearnos con:

```bash
gh auth logout
```

## Documentación sobre placa de desarrollo

En la medida que se desarrollen las distintas actividades, va a ser necesario informacion del hardware que estamos usando. Pueden encontrar esquematico, PCB y otros documentos en este [repositorio](https://github.com/impatrq/rpizerow-labo-kit).

## Documentación sobre modulos de Python

Las bibliotecas de Python de las que vamos a hacer uso pueden encontrarse en el [requirements.txt](requirements.txt). Aqui dejamos links a la documentacion o repositorio de cada una de las bibliotecas:

- [gpiozero](https://pypi.org/project/gpiozero/) para perifericos de la RPiZeroW
- [raspberrypi-tm1637](https://pypi.org/project/raspberrypi-tm1637/) para controlar el display 7 segmentos
- [ADS1x15-ADC](https://github.com/chandrawi/ADS1x15-ADC) para usar el ADC externo
- [Adafruit-BMP](https://github.com/adafruit/Adafruit_Python_BMP) para usar el BMP180
- [requests](https://pypi.org/project/requests/) para hacer consultas por HTTP
