# The-Eighth-Man

(Las librerías necesarias para correr el código están en `requirements.txt`).

1. El archivo `web_scraping.py` descarga los comentarios de la aplicación de Claro. A pesar que en la ventana aparecen 230 000 reseñas, estas condensan las reseñas de todos los países e idiomas (comentarios tanto en español como en inglés), dicho esto, el enlace contiene el fragmento `es_CO`, que se refiere a las reseñas colombianas en español, las cuales son un poco más de 107 000. Estás, con su información relevante, están en el archivo `db_reviews_claro.xlsx`.
2. El archivo donde se procesan estas reseñas es `nlp_model.ipynb`. Primero procesa y limpia las reseñas para dejar solo las palabras relevantes, luego entrena el modelo que predice el número de estrellas de las reseñas, seguido aplicamos un algoritmo de predicción de sentimiento por texto a las reseñas de Claro y añadimos este resultado a una nueva columna. El archivo final `db_reviews_claro_feelings.csv` es exportado para su uso en el API.
3. `main.py` es el archivo principal, detalla la estructura del API y los querys. Para utilizarlo se debe correr en la terminal el comando `uvicorn main:app --reload` y seguir el enlace http://127.0.0.1:8000, por defecto muestra las 10 reseñas más recientes (tomadas el 17 de mayo de 2022), para cambiar el número de reseñas se debe escribir http://127.0.0.1:8000/?n=num_reseñas, donde num_reseñas es el número deseado por ver.

Para acceder al endpoint que predice las estrellas se debe entrar al enlace http://127.0.0.1:8000/docs, allí hay una pestaña verde que dice post, al abrirla y darle click en el boton try out le permitirá editar el request body, reemplace `string` por la reseña que desee y ejecútelo. Más abajo hay un cuadro de response body donde se muestra la reseña, el sentimiento identificado y las estrellas predecidas.

4. Subimos la API un servidor cloud por medio de heroku y el enlace es https://sentimientosnlp.herokuapp.com. Funciona de la misma forma que el enlace local.

Es posible que el enlace falle debido a que implementa algoritmos de inteligencia artificial es muy pesado y sobrepasa el límite con facilidad que heroku permite, esto es así porque es un servicio gratuito.
