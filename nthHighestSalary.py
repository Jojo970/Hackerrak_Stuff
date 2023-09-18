import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    if employee.nunique()["salary"] < N:
        data = {f"getNthHighestSalary({N})": [None]}
        return pd.DataFrame(data = data)

    employee.sort_values(by="salary", inplace=True, ascending = False)
    data = {f"getNthHighestSalary({N})": [pd.unique(employee["salary"])[N-1]]} 
    return pd.DataFrame(data = data)