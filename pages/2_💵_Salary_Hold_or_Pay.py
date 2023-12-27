import streamlit as st
import pandas as pd
import datetime


st.header("Hold or Pay Salary?")
st.divider()


def month_diff(a, b):
    return 12 * (a.year - b.year) + (a.month - b.month)


# last working days selector
last_wd = st.date_input("**Select last working day**", format="DD/MM/YYYY", value=None)


# last payroll cycle of that particular employee
if last_wd and last_wd.day <= 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23)
elif last_wd and last_wd.day > 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23) + pd.DateOffset(months=1)


# get last 6 payroll cycles
if last_wd:
    last_6_payroll_cycles = [
        last_payroll_cycle - pd.DateOffset(months=i) for i in range(0, 7, 1)
    ]

    st.write(f"Last working day : **{last_wd.strftime("%d %B %Y")}**")
    st.write(f"Last payroll cycle : **{last_payroll_cycle.strftime("%d %B %Y")}**")

    for d in last_6_payroll_cycles:
        if month_diff(last_wd, d) < 1:
            st.write(f"- Payroll cycle {d.strftime("%d %b %Y")} : **Hold**")
        elif month_diff(last_wd, d) > 1:
            st.write(f"- Payroll cycle {d.strftime("%d %b %Y")} : **Pay**")