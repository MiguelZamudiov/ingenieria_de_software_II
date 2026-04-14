# Tarea Consumo de APIs - Fase 1 (API REST)

### 1. ¿Qué API elegiste y por qué?
Elegí la PokéAPI. La seleccioné porque es una de las APIs abiertas más completas y estables que existen. Al ser de solo lectura y no requerir tokens, me permitió concentrarme plenamente en entender la estructura de los objetos JSON complejos y en cómo navegar entre diferentes recursos relacionados (como pokémon, habilidades y tipos) sin complicaciones de configuración.

### 2. ¿Qué datos devuelve?
La API responde con objetos JSON muy detallados. Dependiendo del endpoint, devuelve:

* **Información de Pokémon:** Nombre, ID, tipos, estadísticas base, habilidades y URLs a imágenes (sprites).
* **Habilidades:** Descripciones de efectos y qué otros pokémon las poseen.
* **Listados paginados:** Un contador total de registros y enlaces a las "páginas" siguiente y anterior.

### 3. ¿Usa token o no? ¿Qué tipo?
No, esta API es totalmente pública y gratuita. No requiere registro, llaves de API (API Keys) ni Bearer Tokens para acceder a la información.

### 4. ¿Qué código de estado recibiste en cada request?
En todas las peticiones exitosas recibí el código 200 OK. En las pruebas donde intenté buscar un pokémon que no existe (para probar mis tests), recibí un 404 Not Found.

### 5. ¿Qué aprendiste diferente a JSONPlaceholder?
A diferencia de JSONPlaceholder, que maneja estructuras muy planas, con PokéAPI aprendí:

* **Manejo de rutas anidadas:** Entender que un recurso puede llevarte a otro (ej. de la lista de pokémon a la URL de su habilidad específica).
* **Paginación real:** Aprendí a usar limit y offset para no saturar la aplicación con miles de datos de un solo golpe.
* **Navegación de objetos complejos:** Los JSON aquí tienen muchos niveles de profundidad, lo que me obligó a ser más preciso al escribir los tests en Postman para acceder a propiedades específicas.

## Capturas de mis Peticiones y Tests en Postman

### Request 1: GET Listar todos los Pokémon (Paginación):
<img width="1430" height="1002" alt="image" src="https://github.com/user-attachments/assets/97186c58-eca3-4734-bca3-ea29d513fd97" />

### Request 2: GET Obtener Pokémon por Nombre (Pikachu):
<img width="1017" height="956" alt="image" src="https://github.com/user-attachments/assets/90308d7a-7af9-41f5-bd64-3900f43c06e8" />

### Request 3: GET Obtener Habilidad por ID:
<img width="1431" height="939" alt="image" src="https://github.com/user-attachments/assets/5ffc612a-d570-4611-98f1-8651bde09888" />

### Request 4: GET Filtrar Pokémon con límite bajo:
<img width="1281" height="970" alt="image" src="https://github.com/user-attachments/assets/4e60c1dc-cc3e-40ff-98c8-ba2001d93108" />

### Request 5: GET Obtener Tipo de Pokémon (Fire):
<img width="1362" height="941" alt="image" src="https://github.com/user-attachments/assets/736cb668-c21e-44f6-bbf2-d177821e67a2" />
