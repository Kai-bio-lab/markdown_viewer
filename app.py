import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Visualizador Markdown", layout="wide")

def main():
    st.title("📖 Visualizador de Documentos Markdown")
    st.info("Sube tus archivos .md en la barra lateral para comenzar a leer.")
    st.markdown("---")

    # --- BARRA LATERAL (SIDEBAR) ---
    search_term = st.sidebar.text_input("🔍 Buscar palabra clave:", placeholder="Ej. Python...")
    st.sidebar.markdown("---")
    st.sidebar.header("Configuración y Archivos")

    # Componente para cargar múltiples archivos
    uploaded_files = st.sidebar.file_uploader(
        "Carga tus archivos Markdown",
        type=["md"],
        accept_multiple_files=True
    )

    if uploaded_files:
        # Creamos un diccionario para mapear el nombre del archivo con su objeto
        files_dict = {file.name: file for file in uploaded_files}

        # Selector para elegir el archivo a visualizar
        selected_file_name = st.sidebar.pills(
            "Selecciona un archivo para leer:",
            options=list(files_dict.keys()),
            selection_mode = "single"
        )

        # Separador visual en la sidebar
        st.sidebar.markdown("---")
        st.sidebar.write(f"**Archivo activo:** {selected_file_name}")

        # --- ÁREA PRINCIPAL ---
        try:
            # Leemos el contenido del archivo seleccionado
            file_to_read = files_dict[selected_file_name]
            # Es necesario decodificar los bytes del archivo a string (texto)
            content = file_to_read.getvalue().decode("utf-8")

        except KeyError:
            content = ""
            st.info("Selecciona un archivo para visualizar su contenido.")
        # Renderizamos el contenido Markdown
        if search_term:
            # Creamos una etiqueta HTML con fondo verde para el resaltado
            # Usamos replace para envolver la palabra clave en un <span> con estilo
            highlighted_style = f'<span style="background-color: #2ecc71; color: white; padding: 2px 4px; border-radius: 4px;">{search_term}</span>'

            # Reemplazamos el término (sensible a mayúsculas/minúsculas en este caso)
            content = content.replace(search_term, highlighted_style)

            # Informamos cuántas veces aparece (opcional)
            count = content.count(highlighted_style)
            st.sidebar.caption(f"Se encontraron {count} coincidencias.")

        # Renderizamos el contenido (importante: permitir HTML para el resaltado)
        st.markdown(content, unsafe_allow_html=True)
        #st.markdown(content)
    else:
        # Mensaje si no hay archivos cargados
        st.warning("👈 Por favor, carga al menos un archivo .md en la barra lateral.")

if __name__ == "__main__":
    main()
