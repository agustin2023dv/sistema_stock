import streamlit as st
from utils.scanner import escanear_codigo_desde_camara
from utils.db import guardar_producto

st.title("Sistema de Stock")

modo = st.radio("Elegí modo de escaneo:", ["Lectora USB", "Cámara"])

codigo = None

if modo == "Lectora USB":
    codigo = st.text_input("Escaneá un código:")
    if codigo:
        st.success(f"Código leído: {codigo}")

elif modo == "Cámara":
    if st.button("Escanear con cámara"):
        codigo = escanear_codigo_desde_camara()
        if codigo:
            st.success(f"Código leído: {codigo}")

# Mostrar el formulario de carga si hay código
if codigo:
    with st.form("formulario_producto"):
        nombre = st.text_input("Nombre del producto")
        cantidad = st.number_input("Cantidad", min_value=1, step=1)
        submit = st.form_submit_button("Guardar producto")

        if submit:
            if nombre and cantidad:
                guardar_producto(codigo, nombre, int(cantidad))
                st.success("✅ Producto guardado correctamente.")
            else:
                st.warning("⚠️ Completá todos los campos.")
