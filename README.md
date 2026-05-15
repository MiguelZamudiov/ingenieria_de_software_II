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
<img width="677" height="242" alt="parte1_levantar_servidor" src="https://github.com/user-attachments/assets/1fd1d0a2-a2a2-4b54-a6b9-855f00da7443" />

---

### Registrar usuario
<img width="931" height="173" alt="parte1_registrar_usuario" src="https://github.com/user-attachments/assets/805ecab9-220b-43d2-a30c-630d18a06099" />

---

### Login y token
<img width="932" height="177" alt="parte1_hacer_login_guardar_token" src="https://github.com/user-attachments/assets/6bb2df7d-7dac-4f11-a77d-f1fb48398670" />

---

### Consulta de tareas con y sin token
<img width="921" height="401" alt="parte1_consultar_tareas_con_y_sin_token" src="https://github.com/user-attachments/assets/1b2a617a-059f-4922-86e8-54dd710827df" />

---

### Crear tarea
<img width="927" height="298" alt="parte1_crear_tarea" src="https://github.com/user-attachments/assets/2e922846-3105-46da-b616-eecb3b6ec560" />

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
<img width="765" height="122" alt="parte2_se_levanta_la_version_con_solucion" src="https://github.com/user-attachments/assets/05624958-6d86-4cee-8cdd-3e6c2d809d2e" />


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
