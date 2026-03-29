import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    
    sales = pd.read_csv("https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/rossmann-sales.csv")
    # print(sales)
    stores = pd.read_csv("https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/rossmann-stores.csv")
    # print(stores)
    
    stores = stores.set_index("Store")
    # print(stores.head(3))
    
    # print((sales["Open"] == 0).sum())
    # print(sales.loc[sales["Open"] == 1, "Customers"].mean())
    # print(sales.loc[sales["Store"] == 123, "Sales"].sum())
    # print(sales.sort_values("Sales", ascending=False).head(5))
    
    # Is there at least one value in the series that is NaN
    # print(stores.isna().any())
    
    # Completely eliminates all rows which contain a Nan 
    # print(stores.dropna())
    # Can use filna(number) to fill with a specific number, also ffil, bfill and interplate
    
    # print(stores.isna().sum())
    
    stores = stores.fillna(1.000)
    
    # print(stores.loc[stores["CompetitionDistance"].isna()])
    
    # print(stores["CompetitionDistance"].mean())
    
    # sales.info(memory_usage="deep")
    
    sales["Open"] = sales["Open"].astype(bool)
    sales["Promo"] = sales["Promo"].astype(bool)
    sales["SchoolHoliday"] = sales["SchoolHoliday"].astype(bool)
    stores["Promo2"] = stores["Promo2"].astype(bool)
    
    sales["StateHoliday"] = sales["StateHoliday"].astype("category")
    stores["StoreType"] = stores["StoreType"].astype("category")
    stores["Assortment"] = stores["Assortment"].astype("category")

    sales["Date"] = pd.to_datetime(sales["Date"])
    
    print(sales.info(memory_usage="deep"))
    
    # Returns only True rows and then puts them in sales_open
    
    sales_open = sales.loc[sales["Open"]]
    
    sales_open = sales_open.drop(columns=["Open"])
    
    # print(stores["StoreType"].cat.categories)
    
    # print(sales_open["Date"])
    # print(sales_open["Date"].dt.day)

    # print((sales["Date"].dt.month == 7).all() and (sales["Date"].dt.year == 2015).all())

    # print(sales["DayOfWeek"].equals(sales["Date"].dt.weekday + 1))
    
    # Unique values of column
    
    sales_open["DayOfWeek"].unique()

    # number of unique values
    
    # print(sales_open["DayOfWeek"].nunique())
    
    # Value count number of times each value appears
    
    # print(sales_open["DayOfWeek"].value_counts())
    
    # relative quantity of value
    
    # print(sales_open["DayOfWeek"].value_counts(normalize=True))
    
    # include NaN
    
    # print(stores["CompetitionOpenSinceMonth"].value_counts(dropna=False))
    
    # Divides the data into n intervals, then puts the data in these intervals 
    # the minimum is taken and then lowered by 0.1% of the delta of the numbers 
    # to make sure the minimum is included
    # minimum here is 708 so we start from 676.161
    
    print(sales_open["Sales"].min())
    print(pd.cut(sales_open["Sales"], 4))
    
    # you set your boundries
    
    pd.cut(sales_open["Sales"], [0, 10000, 20000, np.inf])
    

if __name__ == "__main__":
    main()
