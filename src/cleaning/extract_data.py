import pandas


def load_data(path: str) -> pandas.DataFrame:
    """
    Load data from a csv file.

    Args:
        path: Path to the csv file.
    
    Returns:
        pandas.DataFrame: Dataframe containing the data.
    """
    return pandas.read_csv(path)