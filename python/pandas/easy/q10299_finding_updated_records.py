"""
Platform: StrataScratch
Difficulty: Easy
Question ID: 10299
Problem:
Find the updated records of employees and their salaries.
Assume salary is non-decreasing over time and the current salary
is the maximum salary per employee.
Return employee id, first name, last name, department ID,
and current salary. Order results by employee ID.

DataFrame: ms_employee_salary
Concepts: groupby, max, sorting
"""

import pandas as pd


def updated_employee_records(
     ms_employee_salary : pd.DataFrame    
    ):
    '''
    Return the most recent salary record for each employee.

    Parameters:
        ms_employee_salary(pd.DataFrame) : Employee salary records includng outdated records.

    Returns:
        pd.DataFrame : Updated employee record, sorted by employee ID
    '''

    #Return the row index where the salary is maximal (preserves exact rows).
    idx = (
        ms_employee_salary
        .groupby('id')['salary']
        .idxmax()
    )

    #Select full row
    result = (
        ms_employee_salary
        .loc[idx, ['id', 'first_name', 'last_name', 'department_id', 'salary']]
        .sort_values('id')
        .reset_index(drop=True)
    )

    return result
    
