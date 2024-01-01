import streamlit as st
from datetime import date
from dateutil.relativedelta import relativedelta

st.header("Age Calculator")
st.write("How old is he?")
st.divider()


col1, col2 = st.columns(2)
with col1:
    dob_date = st.date_input(
        "Select **date of birth**",
        format="DD/MM/YYYY",
        value=None,
        min_value=date(1950, 1, 1),
        max_value=date(2049, 12, 31),
    )
with col2:
    end_date = st.date_input(
        "Select **end date**",
        format="DD/MM/YYYY",
        value="today",
        min_value=date(1950, 1, 1),
        max_value=date(2049, 12, 31),
    )

if dob_date is not None and end_date is not None:
    if end_date <= dob_date:
        # start date must be <= end date
        st.error("DOB must be after end date")
    else:
        age = relativedelta(end_date, dob_date)
        # write the result
        st.subheader("Result")
        st.write(
            f"""
            Age = **{age.years} years {age.months} months {age.days} days**.
        """
        )
