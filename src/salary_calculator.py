import pandas as pd
from tabulate import tabulate

tax_brackets = pd.read_excel("src/ter.xlsx")


def convert_tax_status_to_ter_group(tax_status):
    """Get TER given tax status."""
    ter_map = {
        "TK/0": "TER A",
        "TK/1": "TER A",
        "K/0": "TER A",
        "TK/2": "TER B",
        "TK/3": "TER B",
        "K/1": "TER B",
        "K/2": "TER B",
        "K/3": "TER C",
    }
    return ter_map.get(tax_status, None)


def find_tax_percentage(tax_brackets, gross_salary, tax_status):
    """Find TER given gross salary and TER group."""

    ter_group = convert_tax_status_to_ter_group(tax_status)
    bracket = tax_brackets[
        (tax_brackets["gross_salary_from"] <= gross_salary)
        & (tax_brackets["gross_salary_to"] >= gross_salary)
        & (tax_brackets["ter_group"] == ter_group)
    ]
    if not bracket.empty:
        return bracket.iloc[0]["ter"]
    return None


def calculate_tax(tax_brackets, gross_salary, tax_status):
    """Find tax given gross salary and TER group."""
    ter = find_tax_percentage(tax_brackets, gross_salary, tax_status)
    return round(gross_salary * ter, 0)


def calculate_jht(basic_salary):
    jht_company = 3.7 / 100 * basic_salary
    jht_employee = 2.0 / 100 * basic_salary
    return jht_company, jht_employee


def calculate_jkk(basic_salary):
    jkk_company = 2.4 / 100 * basic_salary
    return jkk_company


def calculate_jkm(basic_salary):
    jkm_company = 0.3 / 100 * basic_salary
    return jkm_company


def calculate_jp(basic_salary):
    jp_company = 2.0 / 100 * min(basic_salary, 10_042_300)
    jp_employee = 1.0 / 100 * min(basic_salary, 10_042_300)
    return jp_company, jp_employee


def calculate_jkn(basic_salary):
    jkn_company = 4.0 / 100 * min(basic_salary, 12_000_000)
    jkn_employee = 1.0 / 100 * min(basic_salary, 12_000_000)
    return jkn_company, jkn_employee
