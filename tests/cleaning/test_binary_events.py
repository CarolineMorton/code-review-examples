from cleaning.binary_events import category_event_to_bool
import pandas as pd


def test_category_event_to_bool():
    test_data = pd.read_csv("tests/test_data/events.csv")
    copd_codes = [195662009, 195967001]
    observed = category_event_to_bool(test_data, "snomed_code", copd_codes, "copd")
    print(observed['copd'].to_list())
    assert observed["copd"].to_list() == [True, True, False, False, False, True, True, True, False, False, False]