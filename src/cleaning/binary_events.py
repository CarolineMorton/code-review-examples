import pandas


def category_event_to_bool(data: pandas.DataFrame, column: str, events: list[int], new_col_name: str) -> pandas.DataFrame:
    """
    Convert a column with a single event to a boolean column.

    Args:
        data: Dataframe with a column to convert.
        column: Column to convert.
        events: List of events that are true
        new_col_name: Name of the new column.

    Returns:
        pandas.DataFrame: Dataframe with a boolean column.
    """
    data[new_col_name] = data.apply(lambda row: row[column] in events, axis=1)
    return data