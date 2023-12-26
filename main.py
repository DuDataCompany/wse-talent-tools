import streamlit as st
import numpy as np
import datetime
import holidays

st.title("TO Tools and Calculator")
st.write("Created : 26 Dec 2023")

# days calculator
st.header("Days Calculator")

# calendar day or working day selector
day_types = st.radio(
    "**Select day type**",
    ["Calendar day", "Working day"],
    captions=["Usual calendar days", "Business days, excluding weekends and holidays"],
)

# date selector
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Select start date", format="DD/MM/YYYY", value=None)
    start_inclusive = st.toggle("Include start date")
with col2:
    end_date = st.date_input("Select end date", format="DD/MM/YYYY", value=None)
    end_inclusive = st.toggle("Include end date")

if start_date is not None and end_date is not None:
    if end_date <= start_date:
        st.error("End date must be after start date")
    else:
        # for calendar day
        if day_types == "Calendar day":
            # by default, the timedelta is not inclusive to both sides
            num_days = end_date - start_date - datetime.timedelta(days=1)
            if start_inclusive:
                num_days += datetime.timedelta(days=1)
            if end_inclusive:
                num_days += datetime.timedelta(days=1)
            num_days = num_days.days

        # for working day
        elif day_types == "Working day":
            # get all holidays between start date and end date
            start_year = start_date.year
            end_year = end_date.year
            all_holidays = {}
            for year in range(start_year, end_year + 1):
                holidays_for_year = holidays.Indonesia(years=year)
                all_holidays.update(holidays_for_year)

            # convert all holidays into an array of datetime
            all_holidays_arr = [np.datetime64(d) for d in list(all_holidays.keys())]

            # by default, the timedelta is not inclusive to both sides
            # however, we need to add timedelta to date to check if holiday
            if start_inclusive:
                start_date -= datetime.timedelta(days=1)
            if end_inclusive:
                end_date += datetime.timedelta(days=1)
            num_days = (
                np.busday_count(start_date, end_date, holidays=all_holidays_arr) - 1
            )

        st.success(f"Days between : **{num_days} days**")
        st.write(all_holidays_arr)
