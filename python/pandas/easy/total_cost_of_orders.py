"""
Platform: Stratascratch
Problem: Total Cost of Orders
Difficulty: Easy
Concepts: pandas merge, groupby, aggregation, sorting

Task:
Calculate the total order cost per customer.
Return:
customer id, first name, and total order cost,
sorted alphabetically by first name. 
"""


import pandas as pd


def total_cost_per_customer(
        customers: pd.DataFrame,
        orders: pd.DataFrame
    ):
    """
    Calculate total order cost per customer.

    Parameters:
        customers(pd.DataFrame) : Customer information.
        orders(pd.DataFrame) : Order information.

    Returns:
        pd.DataFrame : Total order cost per customer, sorted by first name.
    """

    #Merge datasets
    merged_df = pd.merge(
       orders,
       customers,
       how = 'left',
       left_on = 'cust_id',
       right_on = 'id'
    )

    #calculate total_order_cost by each customers, sort by first_name
    result = (
        merged_df
        .groupby(['cust_id', 'first_name'])
        ['total_order_cost'].sum()
        .reset_index()
        .sort_values('first_name')
    )
  
    return result