import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(by="salary", inplace=True, ascending = False)

    if employee.nunique()["salary"] < 2:
        data = {"SecondHighestSalary": [None]}
        return pd.DataFrame(data = data)

    data = {"SecondHighestSalary": [pd.unique(employee["salary"])[1]]} 
    return pd.DataFrame(data = data)