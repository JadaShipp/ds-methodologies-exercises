# Zillow Regression Project
- The overall goal of this project is to demonstrate understanding of the data science prooject workflow and pipeline. This notebook and repo is meant to display:
> * Planning
> * Data Aquisition
> * Preparation
> * Exploration
> * Modeling
> * Delivery

- The premise of this project is to predict the value of a home based on three variables:
> * Square root
> * Number of bedrooms
> * Number of bathrooms

## Planning

> 1. Access the Zillow database in SQL and write a querry that produces results which include only single family homes purchased between May and June 2017 and has no observations with zeros.
> 2. Read the results into pandas and dop any unecessay rows
> 3. Map the data using FIPS number to show the county of each observation
> 4. Explore the data and establish hypotheses.
>> - $H_0$: Bedroom count bathroom count and square footage have no effect on the value of a single-family home
    - $H_a$: Bedroom count bathroom count and square footage have an effect on the value of a single-family home


# Data Dictionary

|    Variable    |        Data Type       |                                  Description                                 |
|:--------------:|:----------------------:|:----------------------------------------------------------------------------:|
| square_feet    | 14989 non-null float64 | The number of square feet in each single family unit                         |
| taxes          | 14989 non-null float64 | The value of the single family unit                                          |
| home_value     | 14989 non-null float64 | The value of the single family unit                                          |
| bedroom_count  | 14989 non-null float64 | The number of bedrooms in each single family unit                            |
| bathroom_count | 14989 non-null float64 | The number of bathrooms in each single family unit                           |
| County         | 14989 non-null object  | Created Column: The county each home is located in determined by FIPS number |
| tax_rate       | 14989 non-null float64 | Created Column: The amount of tax paid divided by the value of the home      |