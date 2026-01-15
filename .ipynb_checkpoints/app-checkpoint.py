import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("Final_Smart_Home_Locations.csv")

st.title("🏠 Smart Home Location Selector")

# City input
city = st.selectbox("Select City", df['City'].unique())

# Filter city data
city_df = df[df['City'] == city]

st.subheader(f"Top Smart Home Locations in {city}")

# Show top 5
top5 = city_df.head(5)[['Area', 'Location_Score_Normalized']]
st.table(top5)
