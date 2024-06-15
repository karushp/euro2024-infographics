import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import function from another data.py
from data import country_performance_WC2014 , plot_goals_scored, display_goal_counts, history


countries = ['Select Team', 'Albania', 'Austria', 'Belgium', 'Croatia',
             'Czechia', 'Denmark', 'England', 'France', 'Georgia', 'Germany',
             'Hungary', 'Italy', 'Netherlands', 'Poland', 'Portugal', 'Romania',
             'Scotland', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Switzerland',
             'Türkiye', 'Ukraine']


# Set up the Streamlit app
st.set_page_config(page_title="Euro Infographics", page_icon="⚽", layout="wide")
st.title("⚽ Euro Infographics")
st.markdown("""
This application shows the history between two selected teams.
""")

# Create two columns for team selection
col1, col2 = st.columns(2)

with col1:
    team1 = st.selectbox("Select Team 1", countries, index=0)

with col2:
    team2 = st.selectbox("Select Team 2", countries, index=0)


#Add a button to trigger the analysis
if st.button("Show Analysis"):
    if team1 == 'Select Team' or team2 == 'Select Team':
        st.write("Please select both teams to display the analysis.")
    else:
        # Apply Plot Goals Scored function on the selected teams
        if team1 != 'Select team' or team2 != 'Select team':
            st.write(f"### Historical Analysis for {team1 if team1 != 'Select Team' else ''} {'and' if team1 != 'Select Team' and team2 != 'Select Team' else ''} {team2 if team2 != 'Select Team' else ''}")
            history(team1, team2)


        # Apply Country Performance WC2014 function on each selected team
        # Adding a frame around the plot
        frame_style = {'width': '100%', 'padding': '20px', 'border': '1px solid #b0c4de', 'border-radius': '5px'}
        with st.frame(style=frame_style):
            if team1 != 'Select Team':
                country_performance_WC2014(team1)
            # if team2 != 'Select Team':
            #     country_performance_WC2014(team2)
