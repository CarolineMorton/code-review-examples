import pandas


def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the BMI.

    Args:
        weight: Weight in kg.
        height: Height in metres.
    
    Returns:
        float: BMI.
    """
    if height < 1 or height > 2.5:
        raise Exception("Height is not sensible")

    return weight / (height ** 2)


def categorise_bmi(bmi: float) -> str:
    """
    Categorise the BMI.

    Args:
        bmi: BMI.
    
    Returns:
        str: BMI category.
    """
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def clean_bmi(data: pandas.DataFrame) -> pandas.DataFrame:
    """
    Clean the BMI column.

    Args:
        data: Dataframe with a BMI column.
    
    Returns:
        pandas.DataFrame: Dataframe with a BMI column.
    """
    data["bmi"] = data.apply(
        lambda row: calculate_bmi(row["weight"], row["height"]), axis=1
    )
    data["bmi_category"] = data.apply(lambda row: categorise_bmi(row["bmi"]), axis=1)
    return data
