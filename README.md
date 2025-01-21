# Bike Rentals Analysis

## Overview
This project analyzes bike rental usage data across different times of the day and days of the week. The primary objective is to uncover patterns, trends, and insights that can inform better operational decisions for bike rental businesses.

The dataset used in this project includes hourly and daily data on bike rentals, with various features such as weather conditions, time-related factors, season, and user categories.

---

## Dataset
The analysis is based on two datasets:
1. **Hourly Data**: Contains bike rental data recorded on an hourly basis.
2. **Daily Data**: Aggregates bike rental data for each day.

### Key Features:
- `datetime`: Timestamp of the rental data (hourly or daily).
- `season`: Season of the year (e.g., spring, summer).
- `holiday`: Whether the day is a holiday (1 = Yes, 0 = No).
- `workingday`: Whether the day is a working day (1 = Yes, 0 = No).
- `weather`: Weather condition (e.g., clear, cloudy, rainy).
- `temp`: Temperature in Celsius.
- `atemp`: Feels-like temperature in Celsius.
- `humidity`: Humidity percentage.
- `windspeed`: Wind speed.
- `casual`: Number of casual (non-registered) users.
- `registered`: Number of registered users.
- `count`: Total number of bike rentals.

---

## Analysis Goals
1. **Identify Rental Patterns**:
   - Knowing rental pattern each hours to gain peek hours rental

2. **Impact of External Factors**:
   - Evaluate the influence of weather and season on bike rentals.
   - Study the effect of holidays and working days on user behavior.

---

## Methods and Tools
- **Programming Language**: Python
- **Libraries**:
  - Data Analysis: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning (if applicable): `scikit-learn`

---

## Results
Key insights and visualizations are summarized in the analysis notebook. Highlights include:
- Peak usage hours and days.
- Seasonal and weather-related impacts on rentals.
- Holiday and working day impacts on rentals.

---
