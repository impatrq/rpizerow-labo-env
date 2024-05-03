# ejercicios-python

En este directorio hay actividades para resolver usando Python. Se prevee explorar los distintos perifericos de la RPiZeroW y poder usar los modulos que estan conectados en la placa de desarrollo.

## Instrucciones

1- Una vez dentro de este directorio (actividades_python), crear un entorno virtual con el comando:

```bash
python -m venv .rpizerow-env
```

Este comando en particular toma tiempo en resolverse.

2- Activar el entorno virtual e instalar los requisitos:

```bash
source .rpizerow-env/bin/activate && python -m pip install -r requirements.txt
```

3- Ir hasta el directorio del ejercicio a resolver. Ejemplo, si quisiera resolver el ejercicio 3 haría:

```bash
cd ej_03
```

4- Resolver el ejercicio propuesto dentro del directorio correspondiente usando el editor `nano` para escribir el código. Para abrir nano y crear un archivo pueden escribir:

```bash
nano main.py
```

Pueden encontrar informacion sobre los comandos basicos de nano en este [link](https://www.cheatsheet.wtf/Nano/).

5- Para salir de nano usar la combinacion de teclas:

    - `Ctrl + X` para salir
    - `y` para decirle de guardar cambios
    - `Enter` para aceptar

6- Para probar el programa, ejecutarlo corriendo el comando:

```bash
python main.py
```

7- Comentar apropiadamente el programa. Pueden ver algunos estandares de como documentar programas en Python en este [link](https://realpython.com/documenting-python-code/).

8- Realizar los commits apropiados segun los estandares convencionales que pueden ver [aqui](https://www.conventionalcommits.org/en/v1.0.0/).

9- Pushear los cambios al repositorio personal siguiendo los pasos de la seccion de `git add, commit y push` del [README](../README.md).
