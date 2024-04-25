#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/init.h>
#include <linux/kthread.h>
#include <linux/sched.h>
#include <linux/delay.h>
#include <linux/sched/signal.h>

// Variables globales para kernel threads
static struct task_struct *kthread_1 = NULL;
static struct task_struct *kthread_2 = NULL;

// TODO:
// Funciones para los hilos

/**
 * @brief Se llama cuando se carga en el kernel
*/
static int __init ej02_module_init(void) {
	// TODO:
	// - Crear ambos hilos
	// - Verificar que se hayan podido crear
	// - Correr hilos
	return 0;
}

/**
 * @brief Se llama cuando se retira del kernel
*/
static void __exit ej02_module_exit(void) {
	// TODO:
	// - Detener hilos
}

// Registro funciones de inicializacion y salida
module_init(ej02_module_init);
module_exit(ej02_module_exit);

// Informacion del modulo (completar lo que corresponda)
MODULE_LICENSE("GPL");
MODULE_AUTHOR("");
MODULE_DESCRIPTION("");
