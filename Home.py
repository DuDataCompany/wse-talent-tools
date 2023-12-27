import datetime
from typing import Literal, Union

import holidays
import numpy as np
import streamlit as st


def main():
    st.title("TO Tools and Calculator")
    st.write("Created : 26 Dec 2023")
    st.divider()

    st.write(
        "This web contains tools to help TO calculate everything about employee.",
        "Select the tool you want on the **left sidebar**."
    )


if __name__ == "__main__":
    main()
