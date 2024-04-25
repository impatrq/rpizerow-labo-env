# ejercicio-01

## Consigna

Hacer un programa que escriba un mensaje el sistema de mensajes del kernel de Linux. Se debe ver un mensaje como el siguiente cuando el modulo se cargue en el kernel:

```
gonzalez_gonzalo_ej01: Hola desde el kernel!
```

Y uno como el siguiente cuando el modulo se retire del kernel:

```
gonzalez_gonzalo_ej01: Chau desde el kernel!
```

Reemplazando el apellido por el correspondiente.

## Instrucciones especiales

- Cambiar el nombre del archivo [apellido_nombre.c](apellido_nombre.c) al que corresponda para el que este resolviendo el ejercicio. Se puede usar el comando:

```bash
mv apellido_nombre_ej01.c gonzalez_gonzalo_ej01.c
```

- Cambiar el valor de la variable `FILE` en el [Makefile](Makefile) poniendo el apellido y nombre que corresponda. Para el caso anterior:

```Makefile
FILE := gonzalez_gonzalo_ej01
```

- Para compilar, cargar el modulo, retirarlo, podemos usar las reglas descritas en el [Makefile](Makefile). Podemos usar el comando:

```bash
make help
```

Para ver que opciones estan disponibles.

- Cuando se haya cumplido con el objetivo, seguir los estandares para hacer un commit y push de los cambios. 
