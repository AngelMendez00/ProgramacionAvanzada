# Programacion Avanzada+

Gestión de Productos con Excepciones Personalizadas y Interfaz Gráfica
Objetivo del Ejercicio
El objetivo de este ejercicio es crear un sistema de gestión de productos para una tienda. Cada producto tendrá un nombre, un precio y una cantidad en inventario. El sistema debe permitir agregar productos, calcular el valor total del inventario y manejar excepciones personalizadas para asegurar que los datos ingresados sean correctos. Además, se debe construir una interfaz gráfica sencilla utilizando tkinter para facilitar la interacción del usuario con el sistema.
 
Requerimientos del Ejercicio
Clase Producto:
 
Atributos:
nombre: El nombre del producto (de tipo str).
precio: El precio del producto (de tipo float).
cantidad: La cantidad disponible en inventario (de tipo int).
Métodos:
calcular_valor_total(): Calcula el valor total del inventario para ese producto, multiplicando la cantidad por el precio.
mostrar_detalles(): Devuelve un string con los detalles del producto, como su nombre, precio, cantidad y valor total.
Excepciones Personalizadas:
 
Se deben crear excepciones personalizadas para manejar los casos en que los datos de entrada no sean válidos:
ProductoInvalidoException: Se lanza cuando el nombre del producto está vacío o es nulo.
PrecioInvalidoException: Se lanza cuando el precio es negativo o cero.
CantidadInvalidaException: Se lanza cuando la cantidad es negativa.
Interfaz Gráfica con tkinter:
 
Usar tkinter para crear una interfaz en la que el usuario pueda ingresar los datos del producto: nombre, precio y cantidad.
Mostrar los detalles del producto o los mensajes de error (en caso de que las excepciones sean lanzadas) en la misma ventana.