import streamlit as st

# Título de la aplicación
st.title("Calculadora Simple")

# Entradas de usuario
num1 = st.number_input("Ingrese el primer número:")
num2 = st.number_input("Ingrese el segundo número:")

# Operaciones
operacion = st.selectbox("Seleccione una operación:", ["Suma", "Resta", "Multiplicación", "División"])

# Botón de cálculo
if st.button("Calcular"):
    if operacion == "Suma":
        resultado = num1 + num2
    elif operacion == "Resta":
        resultado = num1 - num2
    elif operacion == "Multiplicación":
        resultado = num1 * num2
    elif operacion == "División":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Error: No se puede dividir por cero"
    
    # Mostrar resultado
    st.write(f"Resultado: {resultado}")