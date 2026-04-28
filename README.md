# 📖 Markdown Visualizer with Streamlit

Este es un visualizador dinámico e interactivo construido con **Python** y **Streamlit**. Permite cargar, gestionar y leer múltiples archivos Markdown con una interfaz moderna y un sistema de búsqueda con resaltado visual.

---

## ✨ Características

* **Carga Múltiple:** Sube varios archivos `.md` a la vez.
* **Interfaz Moderna:** Selección intuitiva mediante "Pills" en la barra lateral.
* **Buscador en Tiempo Real:** Resalta palabras clave en color verde dentro del documento.
* **Diseño Responsivo:** Modo ancho habilitado para facilitar la lectura de documentos extensos.

---

## 🚀 Instalación de Dependencias

Para ejecutar este proyecto, necesitas tener **Python 3.8+** instalado. Sigue estos pasos para configurar tu entorno:

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/Kai-bio-lab/markdown_viewer.git
    cd tu-repositorio
    ```

2.  **Crea un entorno virtual (Recomendado):**
    ```bash
    # En Windows
    python -m venv .
    .\venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv .
    source ./bin/activate
    ```

3.  **Instala Streamlit o bien mediante el archivo requirements.txt:**
    ```bash
    pip install streamlit
    ```
    o
    ```
    pip install -r requirements.txt
    ```

---

## 💻 Modo de Uso

Sigue estas instrucciones para poner en marcha el visualizador:

1.  **Inicia la aplicación:**
    Desde tu terminal (con el entorno virtual activo), ejecuta:
    ```bash
    streamlit run app.py
    ```

2.  **Carga tus archivos:**
    En la barra lateral izquierda, utiliza el botón **"Browse files"** para subir tus documentos con extensión `.md`.

3.  **Selecciona un documento:**
    Haz clic en los botones de la barra lateral (Pills) para cambiar entre los archivos cargados.

4.  **Busca palabras clave:**
    Escribe cualquier término en el cuadro de búsqueda superior. Verás cómo el texto coincidente se resalta automáticamente en **verde brillante** en el panel principal.

---

## 🛠️ Tecnologías

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)

---
Desarrollado para facilitar la navegación y lectura de documentación técnica.
