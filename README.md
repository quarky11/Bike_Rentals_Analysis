# Bike Rentals Analysis

## Overview
This project analyzes bike rental usage data across different times of the day and days of the week. The primary objective is to uncover patterns, trends, and insights that can inform better operational decisions for bike rental businesses.

The dataset used in this project includes hourly and daily data on bike rentals, with various features such as weather conditions, time-related factors, season, and user categories.

---
## Step to Run Dashboard

### 1 . Steps to Set Up a Virtual Environment
1. Open Command Prompt
   Open CMD by typing cmd in the search bar or pressing Win + R, then typing cmd, and hitting Enter.

2. Navigate to Your Project Directory
   Use the cd command to navigate to your project directory:

   cmd
   cd path\to\your\project

3. Create a Virtual Environment
   Run the following command to create a virtual environment:

   cmd
   python -m venv nameenv  #Replace env with your desired name for the virtual environment folder.

4. Activate the Virtual Environment
   Activate the virtual environment with the following command:

   cmd
   env\Scripts\activate

   Once activated, the CMD prompt will show the virtual environment's name in parentheses, e.g., (env).

---

### 2 . Steps to install packages via requirement.txt

1. ensure already activated the enviroment
2. Run the following command to install all packages listed in the requirements.txt file:

   cmd
   pip install -r requirements.txt

3. After installation, ensure the packages were installed correctly by listing the installed packages:

   cmd
   pip list

---

### 3 . Run Streamlit App on VS CODE

1. If you are using VS Code (my case) dont forget to click open folder and choose Dashboard folder.
2. After that dont forget to Ctrl + Shift + P and select the desired interpreter from the list. This step will connect your library from command prompt to VS Code.
3. After all connect go to terminal and write ' streamlit run app.py '. The 'app.py' is your python file name and in this case that's the name.

---

## Analysis Process

### Dataset
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

### Analysis Goals
1. **Identify Rental Patterns**:
   - Knowing rental pattern each hours to gain peek hours rental

2. **Impact of External Factors**:
   - Evaluate the influence of weather and season on bike rentals.
   - Study the effect of holidays and working days on user behavior.

---

### Methods and Tools
- **Programming Language**: Python
- **Libraries**:
  - Data Analysis: `pandas`
  - Visualization: `matplotlib`, `seaborn`,`plotly`,`streamlit`

---

## Results
Key insights and visualizations are summarized in the analysis notebook. Highlights include:
- Peak usage hours and days.
- Seasonal and weather-related impacts on rentals.
- Holiday and working day impacts on rentals.

---
