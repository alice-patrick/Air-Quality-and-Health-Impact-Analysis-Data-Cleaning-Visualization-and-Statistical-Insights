# Air Quality Data Analysis: Methodology and Findings

This project focuses on the analysis of air quality data to uncover key trends, correlations, and health impacts. The objective is to identify actionable insights for improving air quality and mitigating its harmful effects. The process included data cleaning, feature engineering, and visualizations in Power BI, culminating in evidence-based conclusions and recommendations.

---

## Table of Contents
1. [Introduction](#introduction)  
2. [Dataset](#dataset)  
3. [Objectives](#objectives)  
4. [Tools and Libraries](#tools-and-libraries)  
5. [Methodology](#Methodology)  
6. [Findings](#Findings)  
7. [Results and Insights](#Results-and-Insights)  
8.   [Conclusion and Recommendations](#Conclusion-and-Recommendations)
9. [How to Run the Project](#How-to-Run-the-Project)

---

## Introduction
The air quality is a crucial environmental factor that significantly impacts public health. In this project, we focus on analyzing air quality data to identify trends, correlations between pollutants and weather conditions, and the associated health risks. The goal is to provide insights that could guide air quality management and policy decisions aimed at improving public health outcomes.

---

## Dataset
- **Source:** [Kaggle - Air Quality and Health Impact Dataset](https://www.kaggle.com/datasets/rabieelkharoua/air-quality-and-health-impact-dataset/data)  
- **Size:** Varies (15 columns related to pollutants, weather, and health data)
- **Description:** The dataset contains information on air pollutants (PM2.5, PM10, NO2, O3), weather conditions (temperature, humidity, wind speed), and health impacts (AQI, health impact scores).

## Objectives
1. Perform data cleaning and preprocessing to handle missing values and outliers.
2. Engineer features related to air quality categories and health impact.
3. Conduct correlation analysis to identify relationships between pollutants, weather parameters, and health impact.
4. Visualize the results in Power BI to generate actionable insights for stakeholders.
5. Provide recommendations for improving air quality and mitigating health risks.

---

## Tools and Libraries
- **Python Libraries:** 
- `pandas`, `numpy`: Data manipulation and preprocessing  
- `matplotlib`, `seaborn`: Data visualization    
- **Power BI:** For advanced data visualization  

---

## Methodology
1. **Data Cleaning and Preprocessing**
- Dataset Import: The dataset includes columns representing pollutant levels (e.g., PM2.5, PM10, NO2, SO2, O3), weather parameters (e.g., temperature, humidity, wind speed), and health impact scores.
- Data Imputation: Missing values were handled using statistical imputation techniques to fill gaps and ensure consistency across the dataset.
- Date Conversion: A Date column was created by converting timestamps into a readable format for easier time-series analysis.
- Data Validation: The dataset was checked for any outliers or inconsistencies to ensure high-quality inputs for further analysis.

2. **Feature Engineering**
- Air Quality Categories: Some new calculated columns (AQI SCALE, NO2 SCALE, O3 SCALE, PM1O SCALE, PM2_5 SCALE, SO2 SCALE) were created based on predefined AQI etc thresholds. Categories include "Good," "Moderate," "Unhealthy for Sensitive Groups," "Unhealthy," "Very Unhealthy," and "Hazardous."
- Weather Aggregation: Aggregated weather parameters (temperature, humidity, wind speed) were calculated over time for easier comparison with pollution data.
- Health Impact Score: A Health Impact Score was generated to assess the severity of pollution’s effect on public health, based on AQI values and pollutant concentrations.
  
3. **Correlation Analysis**
- Correlation Study: Correlation between pollutants (AQI,O3, PM1O, PM2.5, NO2, SO2) and weather parameters was performed using 'Scatter Chart'. This identified key relationships, such as the impact of humidity and temperature on pollution levels.
- Findings: Strong correlations were found between elevated temperatures, humidity, and higher pollutant levels, particularly in the "Very Unhealthy" AQI category.

4. **Visualization in Power BI**
- The analysis was visualized in Power BI through a series of dashboards, each designed to provide clear insights into the dataset:
- Air Quality Trends Dashboard: 'Line Chart' and 'Table' displaying time-series data for AQI and pollutant levels during the time.
- Weather and Air Quality Correlation Dashboard: 'Line Chart' and 'Scatter Chart' showing interactions between weather and pollutant levels.
- Health Impact Analysis Dashboard: 'Stacked bar chart' Combining Analysis of Weather, Air Quality, and Health, a 'Scatter and Pie chart' visualising the air quality and health impact and giving an otherview of health cases.
- Key Insights and Recommendations Dashboard: Combined insights from all previous dashboards, supported by stacked bar and column charts.

---

## Findings
1. **Air Quality Trends**
-Peak Values: AQI and O3 showed peak values during summer months (June to August), correlating with higher temperatures. PM2.5 and NO2 also displayed significant variability but with smaller seasonal spikes.
-High Pollution Periods: The months of June to August consistently recorded the highest pollution levels, especially in relation to O3 and AQI.
2. **Correlation Between Weather and Pollution**
-Humidity and Temperature: Higher temperatures and humidity levels were strongly associated with increased pollution, particularly in the "Very Unhealthy" AQI category.
-Wind Speed: Wind speed was found to reduce pollution concentrations across all AQI categories, highlighting its role in improving air quality.
3. **Health Impact**
-Health Impact Scores: The "Very Unhealthy" and "Unhealthy" AQI categories recorded the highest average Health Impact Scores, reflecting severe public health risks.
-Low Impact: "Moderate" and "Good" AQI categories were associated with significantly lower health impact scores, suggesting minimal health risks.
4. **Key Insights**
-Summer Months Critical: The summer months are critical for air quality management due to increased pollution levels and their severe health effects.
-Focus on O3 and NO2: Reducing pollutants like O3 and NO2 should be prioritized to minimize health risks during peak pollution periods.
-Wind Speed's Role: Wind speed plays a key role in mitigating pollution and should be considered when evaluating air quality management strategies.

---

## Results and Insights
- Key Trends: AQI levels were highest during the warmer months, with O3 being the most significant pollutant.
- Health Impact: The most severe health impacts were observed during periods of elevated pollution, particularly in "Very Unhealthy" AQI categories.
- Correlation Analysis: The correlation between higher temperatures, humidity, and increased pollution highlighted the need for weather-based air quality management strategies.
- Model Performance: Preliminary models demonstrated a clear relationship between pollutants and health impacts, emphasizing the potential of predictive tools for air quality monitoring.

---

## Conclusion and Recommendations
**Key Takeaways**
- Pollution Levels: The highest pollution levels occur during warmer months, exacerbating public health risks, particularly in urban areas.
- Health Impact: Health impact is strongly influenced by AQI categories, with the most adverse effects observed in the "Very Unhealthy" and "Unhealthy" zones.
- Weather Impact: Weather parameters, particularly wind speed, are instrumental in reducing pollution concentrations.

**Recommendations**
- Regulations: Stricter regulations should be implemented to limit emissions during the summer months to mitigate air quality degradation.
- Urban Planning: Promote the development of urban greenery and infrastructure that enhances natural ventilation to improve air circulation and reduce pollution levels.
- Public Awareness Campaigns: Raise awareness about high-pollution periods and encourage protective measures, such as reduced outdoor exposure, to safeguard public health.

---

## How to Run the Project  
1. Clone this repository:  
   ```bash
   git clone https://github.com/alice-patrick/Air-Quality-and-Health-Impact-Analysis-Data-Cleaning-Visualization-and-Statistical-Insights.git

![image](https://github.com/user-attachments/assets/5a878a16-2ea2-4b79-abda-d79dcc22609d)

![image](https://github.com/user-attachments/assets/a08ec86c-5e5f-4e3e-9924-ae42e294d46d) 

![image](https://github.com/user-attachments/assets/04826837-f94d-40d1-a14a-4ff2b7da069e)

![image](https://github.com/user-attachments/assets/90b6e13e-6b49-42b9-8760-47e8571683f1)





