# Smart-Home-Location-Selector

## 📌 Project Overview
Choosing a suitable residential location is a complex task as it depends on multiple factors such as safety, pollution, affordability, accessibility, and lifestyle.  
This project proposes a Machine Learning–based system that analyzes these factors and recommends the most suitable smart home locations.

## 🎯 Objectives
- To analyze residential location data using multiple parameters
- To compute a suitability score for each area
- To recommend the best locations using ML techniques
- To provide a simple user interface for viewing recommendations

## 🏙️ Cities Covered
- Delhi NCR  
- Mumbai  
- Bengaluru  
- Hyderabad  
- Pune  
- Chennai  

Each city contains multiple residential areas.

## 📊 Dataset Description
- Type: Synthetic dataset with realistic ranges
- Size: ~20,000 records
- Features include:
  - Safety Score
  - Pollution Index
  - Housing Price
  - Distance to hospitals, schools, metro
  - Lifestyle and green space indicators

City-wise adjustments were applied to improve realism.

## 🧠 Methodology
1. Dataset preparation and verification  
2. Exploratory Data Analysis (EDA)  
3. Score adjustment for realism  
4. Feature normalization (Min–Max Scaling)  
5. Location score computation  
6. Machine Learning model training  
7. Result visualization and ranking  

## 🤖 Machine Learning Model
- Algorithm: Random Forest Regressor
- Target Variable: Normalized Location Score
- Evaluation Metrics:
  - R² Score
  - Mean Absolute Error (MAE)

## 📈 Results
- Top smart home locations were identified for each city
- Feature importance analysis showed key factors influencing location suitability
- ML model achieved good prediction accuracy

## 🖥️ User Interface
A simple UI was developed using **Streamlit** to:
- Select a city
- View top recommended locations

## 🛠️ Technologies Used
- Python  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib  
- Streamlit  

## 🔮 Future Scope
- Integration of real-time data
- Map-based visualization
- Personalized recommendations based on user preferences

## 👩‍💻 Author
Swastika Kumari  


