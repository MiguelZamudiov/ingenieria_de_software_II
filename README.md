# Tarea Consumo de APIs - parte 2 (GraphQL) - Miguel Angel Zamudio Villa


## Análisis y Comparativa

### 1. ¿Qué diferencia encontraste vs REST?
La diferencia fundamental radica en el control sobre la información. Mientras que en REST los endpoints son fijos y suelen devolver un objeto completo con datos que a veces no necesitamos (*Overfetching*), en GraphQL tenemos un punto de entrada único y somos nosotros, mediante la Query, quienes definimos la estructura exacta de la respuesta. Esto optimiza el ancho de banda y simplifica el desarrollo en el cliente, ya que no dependemos de múltiples URLs para obtener datos relacionados.

### 2. ¿Cuántos requests REST necesitarías para reemplazar tu query más compleja?
Para mi "Query combinada" (donde consulto un continente y obtengo la lista de sus países con sus respectivas capitales), en una arquitectura REST tradicional habría necesitado al menos 2 peticiones: una para obtener los detalles del continente y otra distinta para listar los países filtrados por el código de ese continente. Con GraphQL, logré consolidar esta jerarquía en una sola operación POST, reduciendo la latencia y la complejidad del manejo de estados en el frontend.

### 3. ¿En qué proyecto real usarías GraphQL?
Lo implementaría sin duda en una aplicación móvil de alto rendimiento. Debido a que en dispositivos móviles la conexión puede ser inestable, minimizar el número de peticiones al servidor y el tamaño de los paquetes de datos es crítico. También es ideal para plataformas con datos altamente relacionados (como una red social o un e-commerce), donde una sola vista necesita mostrar información de usuarios, comentarios, productos y categorías de forma simultánea.

---

## Capturas de mis Peticiones y Tests en Postman

###Request 1: Query básica (Lista de todos los continentes):
  <img width="1912" height="986" alt="image" src="https://github.com/user-attachments/assets/248c7935-3b86-4a64-a5d5-d61af1568a67" />

###Request 2: Query con filtro por argumento (Datos de un país específico):
  <img width="1891" height="952" alt="image" src="https://github.com/user-attachments/assets/a3e408b7-d350-4967-a389-d4fec5be3260" />

###Request 3: Query anidada (País con su continente y lenguajes oficiales):
  <img width="1904" height="911" alt="image" src="https://github.com/user-attachments/assets/a8bd867d-a05b-4977-90b6-2b1b4b551e19" />

###Request 4: Query de lista completa (Todos los idiomas registrados):
  <img width="1918" height="963" alt="image" src="https://github.com/user-attachments/assets/0e78b7c2-340f-4028-8187-fa33fb83ef60" />

###Request 5: Query combinada (Continente específico y su lista de países):
  <img width="1895" height="943" alt="image" src="https://github.com/user-attachments/assets/79281d9f-850a-4bff-b087-793abee6e038" />


