import streamlit as st
from dateutil.relativedelta import relativedelta

st.header("Penalty Calculator")
st.write("We impose penalty for resigning contract employees.")
st.divider()


# date selector
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input(
        "Select **contract start date**", format="DD/MM/YYYY", value=None
    )
with col2:
    end_date = st.date_input(
        "Select **contract end date**", format="DD/MM/YYYY", value=None
    )

last_working_date = st.date_input(
    "Select **last working date**", format="DD/MM/YYYY", value=None
)


if start_date is not None and end_date is not None and last_working_date is not None:
    if end_date <= start_date:
        # start date must be <= end date
        st.error("Contracr end date must be after start date")
#     else:
#         diff = relativedelta(end_date, start_date)
#         if diff.years >= 7:
#             bonus = "**:green[3x base salary]**."
#         elif diff.years >= 5:
#             bonus = "**:green[2x base salary]**."
#         else:
#             bonus = "**:red[0]**."

#         # write the result
#         st.subheader("Result")
#         st.write(
#             f"""
#             Working period = **{diff.years} years {diff.months} months {diff.days} days**.
#         """
#         )
#         st.write(f"Bonus = {bonus}")
