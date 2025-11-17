# Project Proposal – Forecasting GDP Growth After Natural Disasters

**Project title:** Forecasting GDP Growth After Natural Disasters with Supervised Learning  
**Category:** Custom Project (Machine Learning / Data Analysis & Visualization)

## Problem statement / Motivation

Natural disasters such as earthquakes, floods, and storms create large shocks, and countries often react very differently in terms of future GDP growth. The goal of this project is **not** to estimate a causal effect, but to build a **purely predictive machine learning model** that forecasts **next-year real GDP growth** after disasters using structured data. The focus is on supervised learning, model comparison, and out-of-sample performance, in line with the machine learning tools covered in Advanced Programming. I also want the project to be **interactive**, so that a user can explore the models and results through a simple command-line interface.

## Planned approach and technologies

I will construct a panel-style dataset where each row corresponds to a (country, year, disaster) observation. The features will include: current GDP growth, disaster characteristics (type, magnitude, fatalities, people affected) and country-level indicators (income group, institutional quality). Using NumPy and pandas, I will clean the data, handle missing values and outliers, and build a feature matrix for **supervised regression**.

The core of the project will follow the scikit-learn workflow: splitting the data into train and test sets, building preprocessing pipelines with a `ColumnTransformer` (`StandardScaler` for numeric features and `OneHotEncoder` for categorical features), and fitting several machine learning models. I will compare:
- a **mean baseline** (always predicting the average growth),
- a **linear regression model** implemented in scikit-learn,
- a **RandomForestRegressor** to capture nonlinearities and interactions.

Models will be evaluated with MAE, RMSE and R², and I will report a **formal model comparison table**. An **interactive command-line interface (CLI)** will allow the user to: load the data, train or retrain the models, display the evaluation metrics, and generate plots (e.g. predicted vs actual GDP growth for a selected country) with matplotlib.

## Expected challenges and how I’ll address them

The main challenges are data quality (missing values, extreme observations), the risk of overfitting, and keeping the code modular. I will address these by designing a clear preprocessing pipeline, using a clean train/test split with simple hyperparameters, and organising the project into modules (`data_loading`, `features`, `models`, `evaluation`, `cli`) with a few unit tests using `unittest`.

## Success criteria and stretch goals

The project is successful if:
- the scikit-learn pipelines and the **CLI** run end-to-end without errors;
- the regression models clearly outperform the mean baseline on the test set;
- I can compare models using standard ML metrics and interpret the results with plots produced from the CLI.

If time permits, I plan to experiment with a small `MLPRegressor` (neural network) and add an exploratory K-Means clustering step to group similar country–disaster situations.
