"""
Platform: StrataScratch
Difficulty: Easy
Question ID: 9622
Problem:
Find the average number of bathrooms and bedrooms
for each city's property types.

DataFrame: airbnb_search_details
Concepts: groupby, aggregation, rounding
"""

import pandas as pd


def avg_bathrooms_bedrooms_per_city_property(
    airbnb_search_details: pd.DataFrame
    ):
    """
    Calculate the average number of bathrooms and bedrooms
    for each city and property type.

    Parameters:
        airbnb_search_details (pd.DataFrame):
            Airbnb listing details.

    Returns:
        pd.DataFrame:
            City, property type, average bathrooms and bedrooms.
    """

    result = (
        airbnb_search_details
        .groupby(['city', 'property_type'])[['bathrooms', 'bedrooms']]
        .mean()
        .round(2)
        .reset_index()
        .rename(columns = {
            'bathrooms': 'n_bathrooms_avg',
            'bedrooms': 'n_bedrooms_avg'
        })
    )

    return result