import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
from ultralytics import YOLO
import numpy as np
import threading
import time

# Import function from another data.py
from data import history , country_performance_WC2014 , plot_goals_scored


countries = ['Germany' , 'Scotland' , 'Hungary', 'Switzerland','Spain',
             'Croatia', 'Italy','Albania','Slovenia','Denmark','Serbia',
             'England', 'Netherlands','France','Poland','Austria',
             'Ukraine','Slovakia','Belgium','Romania','Portugal','Czechia',
             'Georgia','Türkiye']

# Set up the Streamlit app
st.set_page_config(page_title="Euro Infographics", page_icon="⚽", layout="wide")
st.title("⚽ Euro Infographics")
st.markdown("""
This application shows the history between two selected teams.
""")

# Select teams
team1 = st.selectbox("Select Team 1", countries)
team2 = st.selectbox("Select Team 2", countries)

# Apply 'Plot goals Scored' function on the selected teams
if team1 and team2:
    st.write(f"### Goals Analysis for {team1} and {team2}")
    plot_goals_scored(team1, team2)

# Apply 'Country Performance WC2014' function on each selected team
if team1:
    country_performance_WC2014(team1)
if team2:
    country_performance_WC2014(team2)
