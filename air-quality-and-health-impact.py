import pandas as pd
import numpy as np
import os
from datetime import timedelta

# Specify the file path (update this to the correct path for your system)
file_path = r'C:\Users\User\Downloads\air_quality_health_impact_data.csv'

# Verify if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File not found: {file_path}. Please check the file path and try again.")

# Load the dataset
data = pd.read_csv(file_path)

# Replace invalid values (e.g., 0, -999, or empty strings) with NaN
data.replace([0, -999, ''], np.nan, inplace=True)

# Check for missing values
missing_summary = data.isnull().sum()
print("Missing values summary:\n", missing_summary)

# Drop rows or columns with too many missing values (threshold = 70%)
data_cleaned = data.dropna(thresh=data.shape[1] * 0.7, axis=0)  # Keep rows with at least 70% valid data
data_cleaned = data_cleaned.dropna(thresh=data_cleaned.shape[0] * 0.7, axis=1)  # Keep columns with at least 70% valid data

# Fill missing values for numeric columns with the median
for column in data_cleaned.select_dtypes(include=[np.number]).columns:
    median_value = data_cleaned[column].median()
    data_cleaned[column] = data_cleaned[column].fillna(median_value)

# Normalize selected numerical columns for better analysis
columns_to_normalize = ['AQI', 'PM10', 'PM2_5', 'NO2', 'SO2', 'O3', 'Temperature', 'Humidity', 'WindSpeed']
for column in columns_to_normalize:
    if column in data_cleaned.columns:
        data_cleaned[column] = (data_cleaned[column] - data_cleaned[column].mean()) / data_cleaned[column].std()

# Add a Date column starting from 2024-01-01
start_date = pd.to_datetime("2024-01-01")
data_cleaned['Date'] = [start_date + timedelta(days=i) for i in range(len(data_cleaned))]

# Check if all values in the 'Date' column are valid datetime values
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'], errors='coerce')

# Check for any invalid date values (which will be NaT after conversion)
invalid_dates = data_cleaned[data_cleaned['Date'].isna()]
print(f"Invalid date values:\n{invalid_dates}")

# Check how many unique dates are in the 'Date' column
unique_dates = data_cleaned['Date'].nunique()
print(f"Number of unique dates: {unique_dates}")

# Ensure that the Date column increments daily
start_date = pd.to_datetime("2024-01-01")
data_cleaned['Date'] = [start_date + timedelta(days=i) for i in range(len(data_cleaned))]

# Save the cleaned dataset for Tableau or Power BI visualization
cleaned_file_path = r'C:\Users\User\Downloads\cleaned_air_quality_data_with_date.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data with Date column saved to: {cleaned_file_path}")

# Basic summary statistics for verification
print("\nSummary statistics of cleaned data:\n", data_cleaned.describe())
