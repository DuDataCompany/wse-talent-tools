import streamlit as st
from dateutil.relativedelta import relativedelta

st.header("Penalty Calculator")
st.write("We impose penalty for resigning contract employees.")
st.divider()


# date selector
col1, col2 = st.columns(2)
with col1:
    contract_start_date = st.date_input(
        "Select **contract start date**", format="DD/MM/YYYY", value=None
    )
with col2:
    contract_end_date = st.date_input(
        "Select **contract end date**", format="DD/MM/YYYY", value=None
    )

last_working_date = st.date_input(
    "Select **last working date**", format="DD/MM/YYYY", value=None
)
base_salary = st.number_input(
    "Insert **base salary**", value=None, placeholder="Base salary"
)


if (
    contract_start_date is not None
    and contract_end_date is not None
    and last_working_date is not None
    and base_salary is not None
):
    if contract_end_date <= contract_start_date:
        # start date must be <= end date
        st.error("Contract end date must be after start date")
    else:
        end_date_to_last_wd = relativedelta(contract_end_date, contract_start_date)
        penalty = end_date_to_last_wd.months * base_salary

        # write the result
        st.subheader("Result")
        st.write(
            f"""
            Remaining contract = **{end_date_to_last_wd.years} years {end_date_to_last_wd.months} months {end_date_to_last_wd.days} days**.
        """
        )
        st.write(f"Penalty = base salary * remaining contract")
        st.write(
            f"Penalty = {base_salary:,.0f} * {end_date_to_last_wd.months} = {base_salary * end_date_to_last_wd.months: ,.0f}"
        )
