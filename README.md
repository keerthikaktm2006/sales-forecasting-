## Sales Forecasting Using Machine Learning
## 🔍 Project Overview
Sales Forecasting is a critical business task that helps organizations plan inventory, manage resources, and optimize revenue.  
This project predicts **future sales** using **historical sales data** and **Machine Learning techniques**, specifically the **Random Forest Regressor**.
The model learns patterns, trends, and seasonality from past data to generate accurate sales predictions.
## 🎯 Objectives
•	 To analyze historical sales data in order to identify trends and seasonal patterns.
•	To preprocess and clean the sales data to ensure accurate and reliable analysis.
•	To develop a machine learning–based sales forecasting model using historical data.
•	To generate accurate sales forecasts that support effective business decision-making.
•	To improve inventory planning and demand management through predictive insights.


## 🧠 Machine Learning Model
- **Algorithm Used:** Random Forest Regressor
- **Why Random Forest?**
  - Handles non-linear relationships effectively
  - Reduces overfitting by combining multiple decision trees
  - Performs well on real-world structured data
  - Provides better accuracy than basic regression models

## 🗂️ Dataset Description

### 📅 Time Period
- The dataset contains historical sales transactions recorded between **2016 and 2017**.

### 📊 Dataset Size
- Approximately **9,900+ rows × 18 columns**

### 🧾 Dataset Attributes

| Column Name     | Description |
|-----------------|-------------|
| Row ID          | Unique identifier for each record |
| Order ID        | Unique identifier for each order |
| Order Date      | Date on which the order was placed |
| Ship Date       | Date on which the order was shipped |
| Ship Mode       | Shipping mode used |
| Customer ID     | Unique customer identifier |
| Customer Name   | Name of the customer |
| Customer Name   | Name of the customer |
| Segment         | Customer segment (Consumer, Corporate, etc.) |
| Country         | Country of sale |
| City            | City of sale |
| State           | State of sale |
| Postal Code     | Postal code of the location |
| Region          | Sales region |
| Product ID      | Unique product identifier |
| Category        | Product category |
| Sub-Category    | Product sub-category |
| Product Name    | Name of the product |
| Sales           | Sales value of the transaction |

## 🧹 Data Preprocessing

The following preprocessing steps were applied to prepare the data for analysis and modeling:

- **Loading the Dataset**  
  The sales dataset was loaded into the Jupyter Notebook using the **Pandas** library.

- **Checking Dataset Structure**  
  Dataset shape, column names, and data types were examined to understand the structure of the data.

- **Handling Missing Values**  
  The dataset was checked for missing or null values, and appropriate handling methods were applied to ensure data consistency.

- **Removing Duplicate Records**  
  Duplicate rows were identified and removed to avoid biased analysis and incorrect predictions.
 **Data Type Conversion**  
  Time-related attributes such as **year, month, day, and weekday** were extracted and converted into numerical format for machine learning suitability.

- **Feature Selection**  
  Relevant features such as **sales, region, segment, and time-based attributes** were selected, while unnecessary columns were removed to improve model efficiency.

- **Outlier Analysis**  
  Extreme sales values were analyzed using statistical methods and visual inspection to minimize their impact on the model.


## 🔄 Project Workflow
1. Data Collection  
2. Data Cleaning & Preprocessing  
3. Exploratory Data Analysis (EDA)  
4. Feature Engineering  
5. Model Training  
6. Model Evaluation  
7. Sales Prediction

## 📈 Exploratory Data Analysis (EDA)
- Analyzed sales distribution
- Identified seasonal trends
- Studied monthly and yearly sales patterns
- Visualized data using graphs for better insights
  ## ⚙️ Technologies Used
- **Programming Language:** Python  
- **Libraries:**
  - Pandas
  - NumPy
  - Scikit-learn
  - Matplotlib
  - Seaborn
- **Development Environment:** Jupyter Notebook
  ## 📊 Model Evaluation
   Model performance evaluated using appropriate regression metrics
- Predictions closely follow actual sales trends
- Suitable for practical forecasting scenarios
Metric	Random Forest Model
MAE	0.84
RMSE	1.03
R² Score	  0.88
## 🚀 Deployment
Deployment Method
- Streamlit framework was used to deploy the sales prediction model.
- The trained Random Forest Regressor model is integrated into a Streamlit web application.
- The interface allows users to enter a specific date (Year, Month, Day) and predict tomorrow’s sales interactively.
- The application also visualizes historical sales trends to help users understand past patterns.
-**Public / Local Access**
- The application is deployed locally and accessed through the browser using:
http://localhost:8501
## 🚀 Results
- The Random Forest model successfully predicts future sales
- Captures both trend and seasonal variations
- Provides valuable insights for business planning
- ## 🔮 Future Enhancements
- Implement advanced models like XGBoost or LSTM
- Deploy the model as a web application
- Add real-time sales data integration
- Improve accuracy using hyperparameter tuning
## 👩‍💻 Author
**Keerthika**  
Aspiring Data Scientist | Machine Learning Enthusiast  
## 📌 Note
This project is created for learning and academic purposes and can be extended for real-world business applications.

   
	

