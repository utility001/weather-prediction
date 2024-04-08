# Daily Weather Forecasting Model for New Delhi, India

## Overview

This repository contains code for using an ARIMAX model forecasting daily weather in New Delhi, India. The model utilizes historical weather data sourced from Kaggle to predict future daily weather conditions.

## Dataset

The dataset used for training and testing the model was obtained from Kaggle. It consists of historical daily weather in the city of New Delhi, India. The 4 parameters here are meantemp, humidity, wind_speed, meanpressure.

**Dataset Source**: [Kaggle](https://www.kaggle.com/datasets/sumanthvrao/daily-climate-time-series-data/data)

## Dependencies

The following Python libraries are required to run the code:

- NumPy
- Pandas
- Matplotlib
- Seaborn
- Statsmodels

## Model Building

The SARIMAX model is built using the `statsmodels` library in Python. The steps involved in building the model include:

1. **Ingest**: Getting the dataset from the source

2. **Exploratory Data Analysis (EDA)**: Analyzing the historical weather data to understand patterns, trends, and seasonality.

3. **Data Preprocessing**: Cleaning the dataset, handling missing values, and preparing the data for model training.
   
4. **Model Selection**: Selecting appropriate parameters and selecting the best model via the Akaike informaton criterion (AIC) which helps to measure the relative information lost in the model

4. **Model Training**: Fitting the SARIMAX model to the training data.

5. **Model Evaluation**: Evaluating the model's performance using the Mean Absolute Error (MAE), and visual inspection of forecasted vs. actual values.

6. **Forecasting**: Generating forecasts for future daily weather conditions based on the trained SARIMA model.

## Results

The model produces daily weather forecasts for New Delhi, India. These forecasts can be used for various applications, such as agriculture, transportation, and urban planning, to make informed decisions based on anticipated weather conditions.