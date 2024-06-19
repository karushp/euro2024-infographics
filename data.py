import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st


# Function to show EURO history for 2 teams
def history(team1,team2):
    # Loding Euro Dataset
    euro_df = pd.read_csv('data/Uefa Euro Cup All Matches.csv')

    # Function to clean Eruo Dataset
    def clean_euro_df(df):
        # Clearing string for Home and Away team
        df['HomeTeamName'] = df['HomeTeamName'].str.strip()
        df['AwayTeamName'] = df['AwayTeamName'].str.strip()
        df['SpecialWinConditions'] = df['SpecialWinConditions'].str.strip()

        df['HomeTeamName'].replace("Turkey","Türkiye", inplace=True)
        df['HomeTeamName'].replace("Czech Republic","Czechia",inplace=True)
        df['AwayTeamName'].replace("Turkey","Türkiye", inplace=True)
        df['AwayTeamName'].replace("Czech Republic","Czechia",inplace=True)

        # Filling NULL value with NA
        df['SpecialWinConditions'].fillna('NA',inplace=True)


    clean_euro_df(euro_df)

    # Keeping only relevant columns
    euro_df = euro_df [['Date',	'Time', 'HomeTeamName', 'AwayTeamName',	'HomeTeamGoals','AwayTeamGoals',
                        'Stage','SpecialWinConditions', 'Year']]

    mask = ((euro_df['HomeTeamName'] == team1) & (euro_df['AwayTeamName'] == team2)) | \
           ((euro_df['HomeTeamName'] == team2) & (euro_df['AwayTeamName'] == team1))


    result = euro_df[mask]
    if result.empty:
        st.write('No data Found')
    else:
        st.table(result)

# Function to plot goals scored between 2 teams
def plot_goals_scored(team1, team2):
    # Loding Euro Dataset
    euro_df = pd.read_csv('data/Uefa Euro Cup All Matches.csv')

    # Function to clean Eruo Dataset
    def clean_euro_df(df):
        # Clearing string for Home and Away team
        df['HomeTeamName'] = df['HomeTeamName'].str.strip()
        df['AwayTeamName'] = df['AwayTeamName'].str.strip()
        df['SpecialWinConditions'] = df['SpecialWinConditions'].str.strip()

        df['HomeTeamName'].replace("Turkey","Türkiye", inplace=True)
        df['HomeTeamName'].replace("Czech Republic","Czechia",inplace=True)
        df['AwayTeamName'].replace("Turkey","Türkiye", inplace=True)
        df['AwayTeamName'].replace("Czech Republic","Czechia",inplace=True)

        # Filling NULL value with NA
        df['SpecialWinConditions'].fillna('NA',inplace=True)

    clean_euro_df(euro_df)

    """
    Plots the goals scored by two teams in their respective matches.

    Parameters:
    team1 (str): The name of the first team.
    team2 (str): The name of the second team.
    matches (pd.DataFrame): DataFrame containing match data with columns 'HomeTeamName', 'AwayTeamName', 'Date', 'HomeTeamGoals', and 'AwayTeamGoals'.
    """

    plt.figure(figsize=(10, 8))

    # Goals scored by Team1
    team1_matches = euro_df[(euro_df['HomeTeamName'] == team1) | (euro_df['AwayTeamName'] == team1)]
    home_team1 = team1_matches[team1_matches['HomeTeamName'] == team1]
    away_team1 = team1_matches[team1_matches['AwayTeamName'] == team1]

    plt.bar(home_team1['Date'], home_team1['HomeTeamGoals'], label=f'{team1} Goals at Home', color='blue')
    plt.bar(away_team1['Date'], away_team1['AwayTeamGoals'], label=f'{team1} Goals Away', color='lightblue')

    # Goals scored by Team2
    team2_matches = euro_df[(euro_df['HomeTeamName'] == team2) | (euro_df['AwayTeamName'] == team2)]
    home_team2 = team2_matches[team2_matches['HomeTeamName'] == team2]
    away_team2 = team2_matches[team2_matches['AwayTeamName'] == team2]

    plt.bar(home_team2['Date'], home_team2['HomeTeamGoals'], label=f'{team2} Goals at Home', color='red')
    plt.bar(away_team2['Date'], away_team2['AwayTeamGoals'], label=f'{team2} Goals Away', color='pink')

    # Plot customization
    plt.xlabel('Match Date')
    plt.ylabel('Goals Scored')
    plt.title(f'Goals Scored by {team1} and {team2} in Matches')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    st.pyplot()

# to show goal count
def display_goal_counts(team1, team2):
        # Loding Euro Dataset
    euro_df = pd.read_csv('data/Uefa Euro Cup All Matches.csv')

    # Function to clean Eruo Dataset
    def clean_euro_df(df):
        # Clearing string for Home and Away team
        df['HomeTeamName'] = df['HomeTeamName'].str.strip()
        df['AwayTeamName'] = df['AwayTeamName'].str.strip()
        df['SpecialWinConditions'] = df['SpecialWinConditions'].str.strip()

        df['HomeTeamName'].replace("Turkey","Türkiye", inplace=True)
        df['HomeTeamName'].replace("Czech Republic","Czechia",inplace=True)
        df['AwayTeamName'].replace("Turkey","Türkiye", inplace=True)
        df['AwayTeamName'].replace("Czech Republic","Czechia",inplace=True)

        # Filling NULL value with NA
        df['SpecialWinConditions'].fillna('NA',inplace=True)

    clean_euro_df(euro_df)

    st.write(f"Goals scored by {team1}:")
    team1_matches = euro_df[(euro_df['HomeTeamName'] == team1) | (euro_df['AwayTeamName'] == team1)]
    home_goals_team1 = team1_matches['HomeTeamGoals'].sum()
    away_goals_team1 = team1_matches['AwayTeamGoals'].sum()
    st.write(f"Total goals at home: {home_goals_team1}")
    st.write(f"Total goals away: {away_goals_team1}")

    st.write(f"Goals scored by {team2}:")
    team2_matches = euro_df[(euro_df['HomeTeamName'] == team2) | (euro_df['AwayTeamName'] == team2)]
    home_goals_team2 = team2_matches['HomeTeamGoals'].sum()
    away_goals_team2 = team2_matches['AwayTeamGoals'].sum()
    st.write(f"Total goals at home: {home_goals_team2}")
    st.write(f"Total goals away: {away_goals_team2}")


# Function to filter and plot data for a specific country
def country_performance_WC2014(country):
    # Import Worldcup 2014 data
    worldcup14_df = pd.read_csv('data/international-fifa-world-cup-2014-brazil-teams-2014-to-2014-stats.csv')

    # Filter Worldcup 2014 data
    worldcup14_filter_df= worldcup14_df[['country','win_percentage','draw_percentage_overall','loss_percentage_ovearll']]

    worldcup14_filter_df['country'].replace("Turkey","Türkiye", inplace=True)
    worldcup14_filter_df['country'].replace("Czech Republic","Czechia", inplace=True)

    # Filter the DataFrame for the specific country
    country_data = worldcup14_filter_df[worldcup14_filter_df['country'] == country]

    if country_data.empty:
        st.write(f"No data available for {country}")
        return

    # Extract percentages
    percentages = country_data[['win_percentage', 'loss_percentage_ovearll', 'draw_percentage_overall']].values.flatten()

    # Define labels for the bars
    labels = ['Win', 'Loss', 'Draw']

    # Create the bar plot
    plt.figure(figsize=(5, 3))
    plt.bar(labels, percentages, color=['green', 'red', 'blue'])

    # Add title and labels
    plt.title(f'World cup 2014 performance of {country}')
    plt.ylabel('Percentage')
    plt.xlabel('Outcome')
    plt.ylim(0,100)

    # Show the plot
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

# Function to plot Euro Statistics
def plot_team_statistics(team_name):
    # Import Euro Data Participation
    participated_df =  pd.read_csv('data/Uefa Euro Cup Participated Teams General Statistics.csv')

    # Filter data
    columns_keep = ['Rank', 'Team','Participations','Played','Win','Draw','Loss']
    participated_df_filter = participated_df[columns_keep]

    participated_df_filter['Team'].replace("Turkey","Türkiye", inplace=True)
    participated_df_filter['Team'].replace("Czech Republic","Czechia", inplace=True)

    # Add New rows to calculate Win, Loss and Draw Percentage on overall Euro games played
    participated_df_filter['Win_percentage'] = round(participated_df_filter['Win']/participated_df_filter['Played'],4)*100
    participated_df_filter['Loss_percentage'] = round(participated_df_filter['Loss']/participated_df_filter['Played'],4)*100
    participated_df_filter['Draw_percentage'] = round(participated_df_filter['Draw']/participated_df_filter['Played'],4)*100

    # Check if team is in the list
    if team_name not in participated_df_filter['Team'].values:
        st.write(f"No data available for {team_name}")
    else:
        # Get the row for the team
        team_stats = participated_df_filter[participated_df_filter['Team'] == team_name].iloc[0]

        # Extract relevant data
        categories = ['Win', 'Loss', 'Draw']
        percentages = [team_stats['Win_percentage'], team_stats['Loss_percentage'], team_stats['Draw_percentage']]

        # Write toal Euro Match played
        st.write(f"Total Euro Games Played: {team_stats['Played']}")
        st.write(f"Euro Rank: {team_stats['Rank']}")

        # Plotting
        plt.figure(figsize=(5, 3))
        plt.bar(categories, percentages, color=['green', 'red', 'blue'])

        # Add title and labels
        plt.title(f'Euro Cup Stats for {team_name}')
        plt.ylim(0,100)
        plt.ylabel('Percentage')

        # Show Plot
        st.pyplot()
