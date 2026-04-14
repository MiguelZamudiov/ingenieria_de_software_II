# Tarea Consumo de APIs - Fase 1 (API REST)

### 1. ¿Qué API elegiste y por qué?
Elegí la PokéAPI. [cite_start]La seleccioné porque es una de las APIs abiertas más completas y estables que existen[cite: 1]. [cite_start]Al ser de solo lectura y no requerir tokens, me permitió concentrarme plenamente en entender la estructura de los objetos JSON complejos y en cómo navegar entre diferentes recursos relacionados (como pokémon, habilidades y tipos) sin fricciones de configuración[cite: 1].

### 2. ¿Qué datos devuelve?
[cite_start]La API responde con objetos JSON muy detallados[cite: 2]. Dependiendo del endpoint, devuelve:

* [cite_start]**Información de Pokémon:** Nombre, ID, tipos, estadísticas base, habilidades y URLs a imágenes (sprites)[cite: 2].
* [cite_start]**Habilidades:** Descripciones de efectos y qué otros pokémon las poseen[cite: 2].
* [cite_start]**Listados paginados:** Un contador total de registros y enlaces a las "páginas" siguiente y anterior[cite: 2].

### 3. ¿Usa token o no? ¿Qué tipo?
[cite_start]No, esta API es totalmente pública y gratuita[cite: 2]. [cite_start]No requiere registro, llaves de API (API Keys) ni Bearer Tokens para acceder a la información[cite: 2].

### 4. ¿Qué código de estado recibiste en cada request?
[cite_start]En todas las peticiones exitosas recibí el código 200 OK[cite: 8]. [cite_start]En las pruebas donde intenté buscar un pokémon que no existe (para probar mis tests), recibí un 404 Not Found[cite: 8].

### 5. ¿Qué aprendiste diferente a JSONPlaceholder?
[cite_start]A diferencia de JSONPlaceholder, que maneja estructuras muy planas, con PokéAPI aprendí[cite: 6, 9]:

* [cite_start]**Manejo de rutas anidadas:** Entender que un recurso puede llevarte a otro (ej. de la lista de pokémon a la URL de su habilidad específica)[cite: 9].
* [cite_start]**Paginación real:** Aprendí a usar limit y offset para no saturar la aplicación con miles de datos de un solo golpe[cite: 4, 9].
* [cite_start]**Navegación de objetos complejos:** Los JSON aquí tienen muchos niveles de profundidad, lo que me obligó a ser más preciso al escribir los tests en Postman para acceder a propiedades específicas[cite: 9].
