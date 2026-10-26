# Opción 1: Python + NumPy + Pyodide

1. Sube `index.html` y `main.py` a la raíz de un repositorio GitHub.
2. En Settings → Pages, selecciona la rama `main` y `/ (root)`.
3. Abre la URL publicada.

Notas:
- El archivo `main.py` es una adaptación del renderizador original: mantiene los cálculos de puntos de la flor, pero sustituye Pygame por un búfer de píxeles que Canvas muestra.
- Requiere Internet para cargar Pyodide y NumPy desde CDN.
- Es experimental y pesado: el render calcula y ordena muchos puntos por fotograma. Se limita a unos 30 FPS; equipos lentos pueden ir más despacio.
- No se usa `from js import document` en el archivo Python: el código Python devuelve un búfer de imagen y JavaScript lo presenta.
