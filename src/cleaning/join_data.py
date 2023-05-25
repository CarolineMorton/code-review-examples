import pandas as pd
from cleaning.extract_data import load_data
from cleaning.continious_variables import clean_bmi
from cleaning.binary_events import category_event_to_bool


# events = load_data("data/events.csv")
# demographics = load_data("data/demographics.csv")

def merge_events_with_demographics(event_path: str, demo_path: str) -> pd.DataFrame:
    """
    Merge the events and demographics dataframes.

    Args:
        event_path: Path to the events csv file.
        demo_path: Path to the demographics csv file.

    Returns:
        pandas.DataFrame: Dataframe containing the merged data.
    """
    events = load_data(event_path)
    demographics = load_data(demo_path)
    return events.merge(demographics, on="id", how="left")


def drop_unneeded_cols(data: pd.DataFrame, cols_to_drop: list) -> pd.DataFrame:
    """
    Drop unneeded columns from the data.

    Args:
        data: Dataframe containing the data.

    Returns:
        pandas.DataFrame: Dataframe containing the data with unneeded columns dropped.
    """
    return data.drop(cols_to_drop, axis=1)


def drop_duplicates(data: pd.DataFrame) -> pd.DataFrame:
    """
    Drop duplicate rows from the data.

    Args:
        data: Dataframe containing the data.

    Returns:
        pandas.DataFrame: Dataframe containing the data with duplicate rows dropped.
    """
    return data.drop_duplicates()

