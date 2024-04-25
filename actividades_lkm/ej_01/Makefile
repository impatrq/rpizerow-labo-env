# Reemplazar por apellido y nombre en minuscula (dejar el ej01)
FILE := apellido_nombre_ej01
# Directorio para archivos de compilacion
MDIR := $(PWD)/build
# Directorio donde estan los modulos del kernel
KDIR := /lib/modules/$(shell uname -r)/build

# Archivo objeto para agregar
obj-m += ${FILE}.o

# Regla de compilacion por defecto
all:
	# Intenta crear el directorio build
	@mkdir -p build;	\
	# Copia el Makefile y codigo fuente
	@cp -f ${FILE}.c Makefile ${MDIR};	\
	cd build;	\
	# Compila
	make -C ${KDIR} M=${MDIR} modules

# Regla para limpiar los archivos compilados
clean:
	@cd build;	\
	make -C ${KDIR} M=${MDIR} clean;	\
	cd .. && rm -rf build

# Carga el modulo en el kernel
insmod:
	@sudo insmod build/${FILE}.ko

# Quita el modulo del kernel
rmmod:
	@sudo rmmod ${FILE}
