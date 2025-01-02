import pandas as pd
from app.utils.file_utils import read_csv


def calculate_expired_rate(effective_annual_rate, target_period, csv_file):
    """
    Calculate the expired period rate from the effective annual rate and desired period for each bank.

    Args:
        effective_annual_rate (float): Effective annual interest rate.
        target_period (int): Desired period in days.
        csv_file (str): Path to CSV file.

    Returns:
        list: Expired period rate for each bank.
    """
    df = read_csv(csv_file)
    expired_rates = []
    for _, row in df.iterrows():
        bank_id = row["banco"]
        expired_rate = ((1 + effective_annual_rate) ** (target_period / 365)) - 1
        expired_rates.append({"bank": bank_id, "expired_rate": expired_rate})
    return expired_rates


def calculate_roi(amount, term_in_days, csv_file):
    """
    Calculate return on investment based on the term and amount.

    Args:
        amount (float): Investment amount.
        term_in_days (int): Investment term in days.
        csv_file (str): Path to CSV file.

    Returns:
        list: Profitability generated in pesos for each bank based on the term.
    """
    df = read_csv(csv_file)
    results = {}
    for _, row in df.iterrows():
        if isinstance(amount, (int, float)) and isinstance(term_in_days, (int, float)):
            if row["minmonto"] <= amount <= row["maxmonto"] and row["minplazo"] <= term_in_days <= row["maxplazo"]:
                profitability = amount * (row["tasa"] / 100) * (term_in_days / 365)
                bank_id = row["banco"]
                if bank_id not in results or profitability > results[bank_id]:
                    results[bank_id] = profitability
    return [{"bank": bank_id, "total_profitability": total_profit} for bank_id, total_profit in results.items()]


def find_rates(amount, term_in_days, bank_file):
    """
    Return the effective annual rates for each bank based on the selected period.

    Args:
        amount (float): Investment amount.
        term_in_days (int): Investment term in days.
        bank_file (str): Path to the CSV file containing bank rates.

    Returns:
        list: Effective annual rates for each bank based on the selected period.
    """
    df = read_csv(bank_file)
    rates = {}
    for _, row in df.iterrows():
        if row["minmonto"] <= amount <= row["maxmonto"] and row["minplazo"] <= term_in_days <= row["maxplazo"]:
            bank_id = row["banco"]
            rate = row["tasa"]
            if bank_id not in rates:
                rates[bank_id] = rate
    return [{"bank": bank_id, "effective_annual_rate": rate} for bank_id, rate in rates.items()]