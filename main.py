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
    
    print(stores["CompetitionDistance"].mean())
    
if __name__ == "__main__":
    main()
