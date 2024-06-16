import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)

# Import function from another data.py
from data import country_performance_WC2014 ,history, plot_team_statistics


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
            st.write(f"### Euro Match History between for {team1 if team1 != 'Select Team' else ''} {'and' if team1 != 'Select Team' and team2 != 'Select Team' else ''} {team2 if team2 != 'Select Team' else ''}")
            history(team1, team2)


        # Apply Plot Team Statistics function on the selected teams

        st.write(f"### Euro Cup Statistics of {team1 if team1 != 'Select Team' else ''} {'and' if team1 != 'Select Team' and team2 != 'Select Team' else ''} {team2 if team2 != 'Select Team' else ''}")
        col3,col4 = st.columns(2)
        with col3:
            if team1 != 'Select Team':
                plot_team_statistics(team1)
        with col4:
            if team2 != 'Select Team':
                plot_team_statistics(team2)


        # Apply Country Performance WC2014 function on each selected team
        # apply inside the column
        st.write(f"### World Cup 2014 Performance of {team1 if team1 != 'Select Team' else ''} {'and' if team1 != 'Select Team' and team2 != 'Select Team' else ''} {team2 if team2 != 'Select Team' else ''}")
        col5,col6 = st.columns(2)
        with col5 :
             if team1 != 'Select Team':
                country_performance_WC2014(team1)
        with col6:
            if team2 != 'Select Team' :
                country_performance_WC2014(team2)
