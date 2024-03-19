# Raspberry Pi Zero W Labo Environment

## Instrucciones

1- Si no lo hemos hecho ya, forkear este repositorio para que tengamos una copia bajo nuestro usuario.

2- Iniciar sesion en la RPiZeroW con ssh a traves de Putty o consola de comandos. El usuario y clave son `rpizerow`. En cuanto al hostname, vamos a acceder con rpizerow-0x.local donde x es el numero de la RPiZeroW que queremos usar.

3- Crear dentro del home de rpizerow un directorio con nuestro apellido.

4- Entrar al directorio personal y clonar el fork de este repositorio como:

```bash
git clone https://github.com/USERNAME/rpizerow-labo-env.git
```

Reemplazando USERNAME por el que corresponda.

5- Navegar hasta el repositorio y crear un entorno virtual como:

```bash
python -m venv .rpizerow-env
```

6- Activar el entorno virtual e instalar los requisitos:

```bash
source .rpizerow-env/bin/activate && python -m pip install -r requirements.txt
```

7- Happy coding!

## GitHub CLI

Vamos a usar GitHub CLI como herramienta para poder autorizar las credenciales cuando intentemos pushear. Instrucciones de como usarlo pueden encontrarlas [aqui](github_cli.md).
