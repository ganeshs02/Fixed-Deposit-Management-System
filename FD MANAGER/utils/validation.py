
# validation.py - This file contains functions to validate user inputs.

import re
from datetime import datetime

def validate_bank_name(bank_name):
    """Validates that the bank name is not empty and contains only alphabets and spaces."""
    if bank_name.strip() == "":
        return False
    if not re.match(r"^[A-Za-z\s]+$", bank_name):  # Corrected the escape sequence
        return False
    return True


def validate_deposit_amount(amount):
    """Validates that the deposit amount is a positive number."""
    try:
        amount = float(amount)
        if amount <= 0:
            return False
        return True
    except ValueError:
        return False

def validate_dates(start_date, maturity_date):
    """Validates that the start and maturity dates are in the correct format and the maturity date is after the start date."""
    try:
        start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        maturity_date_obj = datetime.strptime(maturity_date, '%Y-%m-%d')
        if maturity_date_obj <= start_date_obj:
            return False
        return True
    except ValueError:
        return False
    

def validate_interest_rate(interest_rate):
    """Validates that the interest rate is a positive number."""
    try:
        interest_rate = float(interest_rate)
        if interest_rate <= 0:
            return False
        return True
    except ValueError:
        return False
