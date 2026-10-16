import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…import streamlit as st

st.set_page_config(page_title="Advanced Calculator", layout="centered")

if "history" not in st.session_state:
    st.session_state.history = []

st.title("Advanced Calculator / Gelismis Hesap Makinesi")
st.write("Welcome / Hos geldiniz")

operation = st.selectbox(
    "Choose Operation / Islem Secin:",
    ("Select...", "Addition / Toplama (+)", "Subtraction / Cikarma (-)", "Multiplication / Carpma (*)", "Division / Bolme (/)", "Power / Us Alma (^)")
)

if operation != "Select...":
    col1, col2 = st.columns(2)
    with col1:
        num1 = st.number_input("Enter first number / Birinci sayiyi girin:", value=0.0)
    with col2:
        num2 = st.number_input("Enter second number / Ikinci sayiyi girin:", value=0.0)
    
    if st.butt…v
