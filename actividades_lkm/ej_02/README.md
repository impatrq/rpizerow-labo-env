# ejercicio-02

## Consigna

Hacer un programa que cree dos hilos en el kernel que se alternen para imprimir mensajes en el sistema del kernel. Los mensajes pueden ser:

```
gonzalez_gonzalo_ej02: Hola desde el primer hilo!
```

Y para el otro hilo:

```
gonzalez_gonzalo_ej02: Hola desde el segundo hilo!
```

Reemplazando el apellido y nombre por el correspondiente.

Se deben atender los errores correspondientes al crear los hilos, imprimiendo un mensaje de error adecuado y devolviendo un -1 para indicar el error.

El codigo dene estar apropiadamente comentado.

## Instrucciones especiales

- Cambiar el valor de la variable `MODN` en el [Makefile](Makefile) poniendo el apellido y nombre que corresponda. Por ejemplo:

```Makefile
MODN := gonzalez_gonzalo_ej02
```

- Para compilar, cargar el modulo, retirarlo, podemos usar las reglas descritas en el [Makefile](Makefile). Podemos usar el comando:

```bash
make help
```

Para ver que opciones estan disponibles.

- Cuando se haya cumplido con el objetivo, seguir los estandares para hacer un commit y push de los cambios. 

## Informacion util

- La funcion `kthread_create` es la encargada de crear un hilo mientras que `kthread_stop` es la encargada de detenerlo.
- La funcion `wake_up_process` es la que despierta una tarea.
- La estructura tipica para crear un callback para un hilo suele seguir esta estructura:

```c
static int hilo(void *params) {
	// Creacion de variables

	// Bucle mientras que la tarea no sea detenida
	while(!kthread_should_stop()) {
		// Tareas recurrentes
	}
	// Finalizacion del hilo
	return 0;
}
```

