import pandas as pd
import streamlit as st
from dateutil.relativedelta import relativedelta

st.header("Hold or Pay Last Salary?")
st.write("Salary for resigning employees should be held, with a **minimum withholding of one month's salary**.")
st.divider()


def month_diff(a, b):
    """Find the number of month between two dates (rounded down)."""
    return relativedelta(a, b).months


# last working days selector
last_wd = st.date_input("**Select last working day**", format="DD/MM/YYYY", value=None)


# calculate last payroll cycle of that particular employee
if last_wd and last_wd.day <= 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23)
elif last_wd and last_wd.day > 23:
    last_payroll_cycle = last_wd + pd.DateOffset(day=23) + pd.DateOffset(months=1)


if last_wd:
    # the closing of payroll cycle
    last_6_payroll_cycle_ending = [
        last_payroll_cycle - pd.DateOffset(months=i) for i in range(0, 7, 1)
    ]
    # the corresponding opening of payrol cycle
    last_6_payroll_cycle_beginning = [
        d - pd.DateOffset(months=1) - pd.DateOffset(day=24) for d in last_6_payroll_cycle_ending
    ]

    st.subheader("Result")
    st.write(f"Last working day : **{last_wd.strftime('%d %b %Y')}**")
    st.write(
        f"Last payroll cycle : ", 
        f"**{last_6_payroll_cycle_beginning[0].strftime('%d %b %Y')}** - "
        f"**{last_6_payroll_cycle_ending[0].strftime('%d %b %Y')}**"
    )

    for begin, end in zip(
        last_6_payroll_cycle_beginning, last_6_payroll_cycle_ending
    ):
        if month_diff(last_wd, end) < 1:
            payment_status = "**:red[Hold]**"
        elif month_diff(last_wd, end) >= 1:
            payment_status = "**:green[Pay]**"
        st.write(
            f"- {begin.strftime('%d %b %Y')} - ", 
            f"{end.strftime('%d %b %Y')} :", 
            payment_status
        )

