# test_age_validation.py

import pytest
from age_validator import check_age

# --- Equivalence Classes and Boundary Values from the Poster ---

# ECI: Age < 18 (Invalid Class)
# EC2: 18 <= Age <= 60 (Valid Class)
# EC3: Age > 60 (Invalid Class)

# Test cases are designed to cover:
# 1. Representative values (ECT)
# 2. Boundary values (BVA)

# Format: (test_value, expected_result, test_description)
test_data = [
    # --- Invalid Class (EC1) ---
    (17,      False, "ECT representative value (Invalid) - Too young"),
    (0,       False, "Extreme Invalid Boundary (Too young)"),
    (1,       False, "Near Invalid Boundary (Too young)"),

    # --- Valid Class Boundaries (EC2) ---
    (18,      True,  "Lower Valid Boundary"),
    (19,      True,  "Just above Lower Valid Boundary"),
    (60,      True,  "Upper Valid Boundary"),
    (59,      True,  "Just below Upper Valid Boundary"),

    # --- Valid Class Representative (ECT) ---
    (35,      True,  "ECT representative value (Valid)"),

    # --- Invalid Class (EC3) ---
    (61,      False, "ECT representative value (Invalid) - Too old"),
    (100,     False, "Extreme Invalid Boundary (Too old)"),
]

@pytest.mark.parametrize("age, expected_status, description", test_data)
def test_age_verification(age, expected_status, description):
    """
    Tests the check_age function using Equivalence Class and Boundary values.
    """
    actual_status = check_age(age)
    
    # Assert that the actual result matches the expected result
    assert actual_status == expected_status, f"Test failed for Age {age} ({description}). Expected: {expected_status}, Actual: {actual_status}"