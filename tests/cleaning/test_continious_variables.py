from cleaning.continious_variables import calculate_bmi, categorise_bmi, clean_bmi

import pytest


def test_calculate_bmi():
    observed = calculate_bmi(70, 1.70)
    assert observed == 24.221453287197235


def test_calculate_bmi_zero_height():
    with pytest.raises(Exception):
        calculate_bmi(70, 0)


def test_category_bmi_normal():
    observed = categorise_bmi(24)
    assert observed == "normal"

# import pandas as pd
# def test_clean_bmi():
#     test_data = pd.read_csv("tests/test_data/demographics.csv")
#     observed = clean_bmi(test_data)
#     print(obpserved)
#     assert observed['bmi_category'].iloc[0] == "normal"
#     assert observed['bmi_category'].to_list() == ['normal', 'overweight', 'overweight', 'normal', 'obese']
