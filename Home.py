import streamlit as st


def main():
    st.title("TO Tools and Calculator")
    st.write("Created : 26 Dec 2023")
    st.write("Updated : 8 Jun 2024")
    st.divider()

    st.write(
        """
        This website provides tools to make employee calculations easy. 
        Choose the tool you need from the left sidebar.
    """
    )
    st.write(
        """
        Tools selection:
        1. **📅 Days Calculator**: Find the number of days between two dates.
        2. **💰 Last Salary Hold or Pay**: Decide whether to hold or pay the salary of a resigning employee.
        3. **🎉 Bonus Calculator**: Calculate the bonus received by an employee.
        4. **⚖️ Penalty Calculator**: Calculate the penalty for a contract employee who resigns.
        5. **👴🏻 Age Calculator**: Find the age from DOB.
        6. **💸 SalaryCalculator**: Calculate THP given a base salary.
    """
    )


if __name__ == "__main__":
    main()
