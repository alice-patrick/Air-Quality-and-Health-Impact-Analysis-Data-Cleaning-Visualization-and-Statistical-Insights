import pandas as pd
import numpy as np
import os

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
data_cleaned = data_cleaned.dropna(thresh=data.shape[0] * 0.7, axis=1)  # Keep columns with at least 70% valid data

# Ensure correct data types for filling missing values
for column in data_cleaned.select_dtypes(include=[np.number]).columns:
    median_value = data_cleaned[column].median()
    data_cleaned[column].fillna(median_value, inplace=True)

# Normalize selected numerical columns for better analysis
columns_to_normalize = ['AQI', 'PM10', 'PM2_5', 'NO2', 'SO2', 'O3', 'Temperature', 'Humidity', 'WindSpeed']
data_cleaned[columns_to_normalize] = (
    data_cleaned[columns_to_normalize] - data_cleaned[columns_to_normalize].mean()
) / data_cleaned[columns_to_normalize].std()

# Save the cleaned dataset for Tableau visualization
cleaned_file_path = r'C:\Users\User\Downloads\cleaned_air_quality_data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to: {cleaned_file_path}")

# Basic summary statistics for verification
print("\nSummary statistics of cleaned data:\n", data_cleaned.describe())
