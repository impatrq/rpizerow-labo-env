# Nombre del archivo
FILE := main
# Nombre del modulo (reemplazar nombre y apellido)
MODN := apellido_nombre_ej02
# Directorio para archivos de compilacion
MDIR := $(PWD)/build
# Directorio donde estan los modulos del kernel
KDIR := /lib/modules/$(shell uname -r)/build

# Archivo objeto para agregar
obj-m += ${MODN}.o
${MODN}-objs := ${FILE}.o

# Regla de compilacion por defecto
all:
	@mkdir -p build;	\
	cp -f ${FILE}.c Makefile ${MDIR};	\
	cd build;	\
	make -C ${KDIR} M=${MDIR} modules	\

# Regla para limpiar los archivos compilados
clean:
	@cd build;	\
	make -C ${KDIR} M=${MDIR} clean;	\
	cd .. && rm -rf build

# Carga el modulo en el kernel
insmod:
	@sudo insmod build/${MODN}.ko

# Quita el modulo del kernel
rmmod:
	@sudo rmmod ${MODN}

# Miro mensajes del kernel
dmesg:
	@dmesg -wHT | grep ${MODN}

# Ayuda con comandos
help:
	@echo "RPiZeroW Labo Env - Makefile v1.0"
	@echo ""
	@echo "-all: compila el programa (opcion por defecto)"
	@echo "-clean: limpia los archivos compilados"
	@echo "-insmod: carga el modulo en el kernel"
	@echo "-rmmod: retira el modulo del kernel"
	@echo "-dmesg: muestra los mensajes del kernel generados por este modulo"
	@echo "-help: muestra estos mensajes de ayuda"
