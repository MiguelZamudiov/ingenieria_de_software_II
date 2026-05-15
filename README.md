# ingenieria_de_software_II

        NOMBRE                        CORREO

Miguel Angel Zamudio Villa   |  mizamudiovunal.edu.co

# Entrega: Patrones de Diseño

En esta entrega desarrollé tres ejercicios donde apliqué patrones de diseño vistos en clase. La idea fue resolver cada caso de forma simple, separando el código por clases y evitando poner toda la lógica dentro del bloque principal.

## Estructura general del proyecto

- `punto1_singleton/`: ejercicio con patrón creacional Singleton.
- `punto2_factory_adapter/`: ejercicio con un patrón creacional combinado con uno estructural.
- `punto3_factory_facade_strategy/`: ejercicio con un patrón creacional, uno estructural y uno de comportamiento.
- `evidencias/`: capturas de la ejecución de cada punto.

---

## Punto 1 — Singleton

En este primer ejercicio implementé un Singleton sencillo usando Python.

La clase principal solo permite una única instancia durante toda la ejecución del programa. Para lograrlo, se usa una variable de clase que guarda el objeto creado y el método `__new__`, que controla si la instancia ya existe o si debe crearse por primera vez.

### ¿Qué demuestra?
Este punto muestra cómo una clase puede centralizar un recurso compartido, en este caso un logger, evitando que se creen múltiples objetos innecesarios.

### Evidencia
<img width="399" height="95" alt="image" src="https://github.com/user-attachments/assets/1e5aa34e-c8b6-4027-9245-40e84dbfcb5a" />

---

## Punto 2 — Factory + Adapter

En este segundo ejercicio combiné un patrón creacional con uno estructural.

Usé `Factory` para decidir qué tipo de pago crear, y `Adapter` para adaptar un sistema antiguo de pagos a la interfaz moderna del programa.

### ¿Qué demuestra?
La fábrica se encarga de crear el objeto correcto según el método de pago, mientras que el adaptador traduce el comportamiento de un sistema viejo para que pueda usarse igual que los demás objetos del programa.

### Evidencia
<img width="375" height="62" alt="image" src="https://github.com/user-attachments/assets/efc902be-8495-42a2-8be7-e89446749dc4" />

---

## Punto 3 — Factory + Facade + Strategy

En este tercer ejercicio combiné tres patrones distintos.

Usé `Factory` para crear la estrategia de descuento, `Strategy` para cambiar la forma de calcular el descuento según el tipo de cliente, y `Facade` para simplificar todo el proceso de compra en un solo método.

### ¿Qué demuestra?
Este ejercicio muestra cómo se puede separar la creación, el comportamiento y la simplificación de una tarea en clases distintas que trabajan juntas de forma clara.

### Evidencia
<img width="385" height="179" alt="image" src="https://github.com/user-attachments/assets/d67c9691-7f2a-47be-a305-8cf078c02e1f" />

---

## Conclusión

Con estos ejercicios muestro cómo los patrones de diseño ayudan a organizar el código, separando responsabilidades y haciendo que el programa sea más fácil de mantener y explicar.
