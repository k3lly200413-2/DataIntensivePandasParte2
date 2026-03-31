Laboratory exercise for the course *Programmazione di Applicazioni Data Intensive*  
Laurea in Ingegneria e Scienze Informatiche — DISI, Università di Bologna, Cesena  
Proff. Gianluca Moro, Roberto Pasolini

---

## Description

Preprocessing and exploratory data analysis of the **Rossmann pharmacy** chain sales using pandas. The dataset includes historical sales records from 1,115 stores over July 2015, alongside general store information from the 2015 **Kaggle** competition.
Data is provided as two CSV files (`rossmann-sales.csv`, `rossmann-stores.csv`) containing the following information: `daily sales figures`, `customer counts`, `open/closed status`, `promotions`, `holidays`, `store type` and `assortment level`, `competition distance`, and `promotional program participation`.

## Structure

The laboratory is divided into five exercises of increasing complexity:

**Pandas Recap** - boolean filtering, conditional aggregation, and row selection on a DataFrame

**Missing Values** — counting, locating, and imputing `NaN`s in a DataFrame

**Datetime Handling** — extracting date components and validating temporal consistency across columns

**Exploratory Analysis** — computing derived metrics, summarising distributions, and discretising continuous values

**Data Visualisation** — pie charts, histograms, box plots, and scatter plots for distribution and correlation analysis

---

## Requirements

```
numpy
pandas
matplotlib
jupyter
```

Install with:

```bash
pip install numpy pandas matplotlib jupyter
```

---

## Usage

```bash
jupyter notebook
```

The dataset is downloaded automatically on the first run. Source: [Rossmann Stores](https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/rossmann-stores.csv) and [Rossmann Sales](https://github.com/datascienceunibo/dialab2024/raw/main/Preprocessing_con_pandas/rossmann-sales.csv)
