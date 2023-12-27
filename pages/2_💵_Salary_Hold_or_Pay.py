import streamlit as st
import pandas as pd
import datetime


st.header("Days Calculator")
st.divider()

# last working days selector
last_wd = st.date_input("**Select last working day**", format="DD/MM/YYYY", value=None)

# create payroll cycles
dates_24 = [
    datetime.date(2022, 12, 24) + pd.DateOffset(months=i) for i in range(1, 10, 1)
]
dates_23 = [
    d + pd.DateOffset(months=1) - pd.DateOffset(days=1) for d in dates_24
]
payrol_cycles = list(zip(dates_24, dates_23))


if last_wd and last_wd.day <= 24:    
    last_payroll_cycle = last_wd + pd.DateOffset(day=24)
elif last_wd and last_wd.day > 24:
    last_payroll_cycle = last_wd + pd.DateOffset(day=24) + pd.DateOffset(months=1)

# # payroll closing date
# def get_last_n_24th_dates(reference_date, n):
#     result_dates = []

#     for _ in range(n):
#         if reference_date.day >= 24:
#             reference_date = reference_date.replace(day=24)
#         elif reference_date.day < 24:
#             reference_date = (reference_date - pd.DateOffset(months=1)).replace(day=24).to_pydatetime()
#         result_dates.append(reference_date)

#         # move to the previous month
#         reference_date -= datetime.timedelta(days=1)

#     return result_dates

# def month_diff(a, b):
#     return 12 * (a.year - b.year) + (a.month - b.month)

# if last_wd:
#     last_6_closing_dates = get_last_n_24th_dates(last_wd, 6)
#     for d in last_6_closing_dates:
#         if month_diff(last_wd, d) == 0:
#             st.write(f"{d.strftime("%b %Y")} : **Hold**")
#         elif month_diff(last_wd, d) > 0:
#             st.write(f"{d.strftime("%b %Y")} : **Pay**")
