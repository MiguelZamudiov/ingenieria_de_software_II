# ingenieria_de_software_II

        NOMBRE                        CORREO

Miguel Angel Zamudio Villa   |  mizamudiovunal.edu.co

# Taller APIs — Ingeniería de Software

## Introducción

En este laboratorio se trabajó una API desarrollada en Node.js utilizando autenticación con JWT y manejo de endpoints protegidos. Durante la práctica se realizaron pruebas locales y también pruebas remotas mediante SSH desde otro dispositivo.

El laboratorio se dividió en dos partes:
- pruebas locales de la API
- validación de PUT y DELETE usando la versión completa del servidor y conexión remota por SSH

---

# Herramientas utilizadas

- Node.js
- Visual Studio Code
- PowerShell / CMD
- curl
- JWT
- SSH
- GitHub

---

# Parte 1 — Pruebas locales de la API

En la primera parte se realizaron las pruebas básicas del funcionamiento de la API en el computador local.

Las pruebas realizadas fueron:

- levantar el servidor
- registrar un usuario
- iniciar sesión
- obtener el token JWT
- consultar tareas
- crear tareas

---

## Evidencias Parte 1

### Levantar servidor
![Levantar servidor](evidencias/parte1_levantar_servidor.png)

---

### Registrar usuario
![Registrar usuario](evidencias/parte1_registrar_usuario.png)

---

### Login y token
![Login y token](evidencias/parte1_hacer_login_guardar_token.png)

---

### Consulta de tareas con y sin token
![Consulta tareas](evidencias/parte1_consultar_tareas_con_y_sin_token.png)

---

### Crear tarea
![Crear tarea](evidencias/parte1_crear_tarea.png)

---

# Parte 2 — PUT, DELETE y conexión SSH

En esta parte se trabajó con la versión solucionada del servidor para validar los métodos PUT y DELETE.

También se realizó una conexión SSH desde otro dispositivo para ejecutar los comandos de forma remota y comprobar que los endpoints funcionaban correctamente.

Para esta parte:
- el portátil funcionó como servidor
- el celular se utilizó para conectarse por SSH y ejecutar los comandos remotamente

Las pruebas realizadas fueron:
- levantar el servidor solución
- registrar usuario
- hacer login
- crear tarea
- actualizar tarea con PUT
- eliminar tarea con DELETE
- conexión remota por SSH

---

## Evidencias Parte 2

### Levantar versión con solución
![Servidor solución](evidencias/parte2_se_levanta_la_version_con_solucion.png)

---

### Registro de usuario
![Registro usuario](evidencias/parte2_register.png)

---

### Login y obtención del token
![Login token](evidencias/parte2_login_token.png)

---

### Crear tarea
![Crear tarea](evidencias/parte2_crear_tarea.png)

---

### Actualizar tarea con PUT
![PUT](evidencias/parte2_put.png)

---

### Eliminar tarea con DELETE
![DELETE](evidencias/parte2_delete.png)

---

### Conexión SSH desde el celular
![SSH conexión](evidencias/parte2_ssh_conexion.png)

---

### Ejecución remota de comandos
![SSH comandos](evidencias/parte2_ssh_comandos.png)

---

# Conclusiones

Con este laboratorio se pudo entender mejor cómo funciona una API protegida con JWT y cómo se manejan endpoints autenticados mediante tokens.

También se realizaron pruebas con los métodos GET, POST, PUT y DELETE, validando el flujo completo de autenticación y manejo de tareas.

Finalmente, se logró establecer una conexión SSH desde otro dispositivo y ejecutar los comandos remotamente, comprobando el funcionamiento de la API en red local.
