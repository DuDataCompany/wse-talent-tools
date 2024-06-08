import pandas as pd
from tabulate import tabulate
from pprint import pprint

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


def calculate_jht(base_salary):
    jht_company = round(3.7 / 100 * base_salary, 0)
    jht_employee = round(2.0 / 100 * base_salary, 0)
    return jht_company, jht_employee


def calculate_jkk(base_salary):
    jkk_company = round(0.24 / 100 * base_salary, 0)
    return jkk_company


def calculate_jkm(base_salary):
    jkm_company = round(0.3 / 100 * base_salary, 0)
    return jkm_company


def calculate_jp(base_salary):
    jp_company = round(2.0 / 100 * min(base_salary, 10_042_300), 0)
    jp_employee = round(1.0 / 100 * min(base_salary, 10_042_300), 0)
    return jp_company, jp_employee


def calculate_jkn(base_salary):
    jkn_company = round(4.0 / 100 * min(base_salary, 12_000_000), 0)
    jkn_employee = round(1.0 / 100 * min(base_salary, 12_000_000), 0)
    return jkn_company, jkn_employee


def calculate_thp(tax_brackets, base_salary, tax_status, insurance_premium):
    jht_company, jht_employee = calculate_jht(base_salary)
    jkk_company = calculate_jkk(base_salary)
    jkm_company = calculate_jkm(base_salary)
    jp_company, jp_employee = calculate_jp(base_salary)
    jkn_company, jkn_employee = calculate_jkn(base_salary)
    gross_salary = (
        base_salary + insurance_premium + jkk_company + jkm_company + jkn_company
    )
    tax = calculate_tax(tax_brackets, gross_salary, tax_status)
    thp = base_salary - jht_employee - jp_employee - jkn_employee - tax

    return {
        "jht_company": jht_company,
        "jht_employee": jht_employee,
        "jkk_company": jkk_company,
        "jkm_company": jkm_company,
        "jp_company": jp_company,
        "jp_employee": jp_employee,
        "jkn_company": jkn_company,
        "jkn_employee": jkn_employee,
        "gross_salary": gross_salary,
        "tax": tax,
        "thp": thp,
    }


pprint(calculate_thp(tax_brackets, 45_000_000, "TK/0", 307_145))
