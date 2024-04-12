# ejercicio-04

## Consigna

- Hacer dos lecturas analogicas con el ADS1115 incluido en el kit, una del potenciometro y otra del termistor. Se deben comparar ambas mediciones y hacer una especie de control proporcional.

- El valor del potenciometro debe escalarse a un valor de temperatura entre 0 y 30 grados centigrados.

- Cuando la temperatura real este por arriba del valor de temperatura fijada por el potenciometro, se debe encender el LED azul con un brillo proporcional a la diferencia de temperatura.

- Cuando la temperatura real este por abajo del valor de temperatura fijada por el potenciometro, se debe encender el LED rojo con un brillo proporcional a la diferencia de temperatura.

- El brillo debe ser maximo cuando diferencia sea de 5 grados.

- Mostrar en la consola el valor de temperatura indicada por el termistor y el potenciometro para contrastar.

- Resolverlo en un unico `main.py`. Para probarlo, deben usar el comando:

```bash
python main.py
```

- Documentar el programa apropiadamente con los [estandares](https://realpython.com/documenting-python-code/) de Python.

- Hacer el commit correspondiente segun los [estandares convencionales](https://www.conventionalcommits.org/en/v1.0.0/).
