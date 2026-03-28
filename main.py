import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    
    sales = pd.read_csv("https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/rossmann-sales.csv")
    # print(sales)
    stores = pd.read_csv("https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/rossmann-stores.csv")
    print(stores)
    
if __name__ == "__main__":
    main()
