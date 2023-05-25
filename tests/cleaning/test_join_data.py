from cleaning.join_data import merge_events_with_demographics, drop_unneeded_cols
import pandas as pd


EVENTS_PATH = "tests/test_data/events.csv"
DEMOGRAPHICS_PATH = "tests/test_data/demographics.csv"


def test_merge_events_with_demographics():
    observed = merge_events_with_demographics(EVENTS_PATH, DEMOGRAPHICS_PATH)
    assert observed.shape == (11, 5)
    print(observed.columns.to_list())
    assert observed.columns.to_list() == ['id', 'snomed_code', 'snomed_term', 'height', 'weight']

# def test_drop_unneeded_cols():
#     data = pd.read_csv(EVENTS_PATH)
#     observed = drop_unneeded_cols(data, ["id"])
#     assert observed.columns.to_list() == ['snomed_code', 'snomed_term']

