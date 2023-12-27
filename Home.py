import datetime
from typing import Literal, Union

import holidays
import numpy as np
import streamlit as st


def main():
    st.title("TO Tools and Calculator")
    st.write("Created : 26 Dec 2023")
    st.divider()

    st.write("""
        This website provides tools to make employee calculations easy. 
        Just choose the tool you need from the left sidebar.
    """)
    st.write("""
        Tools selection:
        1. **📅 Days Calculator**: Find the number of days between two dates.
        2. **💰 Last Salary Hold or Pay**: Decide whether to hold or pay the salary of a resigning employee.
        3. **🎉 Bonus Calculator**: Calculate the bonus received by an employee.
        4. **⚖️ Penalty Calculator**: Calculate the penalty for a contract employee who resigns.
        5. **🏥 Insurance Premium Calculator**: Calculate the monthly insurance premium from the yearly amount.
    """)


if __name__ == "__main__":
    main()
