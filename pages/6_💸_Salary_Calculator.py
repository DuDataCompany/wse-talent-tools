import streamlit as st

st.header("Salary Calculator")
st.write("Use this to find out THP given a base salary.")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.write("Input the information here:")
    base_salary = st.number_input("Base salary", value=None, placeholder=0)
    tax_status = st.selectbox(
        "Tax/marriage status",
        (
            "TK/0",
            "TK/1",
            "TK/2",
            "TK/3",
            "K/0",
            "K/1",
            "K/2",
            "K/3",
        ),
    )
    insurance = st.number_input(
        "Monthly insurance premium",
        value=None,
        placeholder=0,
    )
    bpjs_kes = st.checkbox("BPJS Kes")
    bpjs_tk = st.checkbox("BPJS TK")

with col2:
    st.write("See the calcualtion here:")
