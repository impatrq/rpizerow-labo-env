#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>

/**
 * @brief Se llama cuando se carga en el kernel
*/
static int __init ej01_module_init(void) {
	// Completar

	// Salio todo bien
	return 0;
}

/**
 * @brief Se llama cuando se retira del kernel
*/
static void __exit ej01_module_exit(void) {
	// Completar

}

// Registro funciones de inicializacion y salida
module_init(ej01_module_init);
module_exit(ej01_module_exit);

// Informacion del modulo (completar lo que corresponda)
MODULE_LICENSE("GPL");
MODULE_AUTHOR("");
MODULE_DESCRIPTION("");
