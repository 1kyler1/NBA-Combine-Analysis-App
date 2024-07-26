import pandas as pd
import streamlit as st
import plotly.express as px


# reads in the csc file and stores it in variable df
df = pd.read_csv("player_combine_stats.csv")

# dropped comus that are unecessary
df = df.drop(columns=['PLAYER_ID', 'TEMP_PLAYER_ID'])

# Fill missing values with "Stats not available"
df.fillna("Stats not available", inplace=True)

# title for the app
st.set_page_config(layout= "centered")
st.title("NBA Combine Player Analysis")

# allows user to pick the year
year = st.selectbox(
    "Choose Your Year", 
    df["SEASON_YEAR"].unique()) # accesses the year category from the dataframe

filtered_df = df[df["SEASON_YEAR"] == year]

# allows users to pick 5 players to view from that year
selected_players = st.multiselect(
    "Select up to three players (From the same year)",
    filtered_df['PLAYER_NAME'].unique(),
    max_selections=3
)

# filter the dataframe based on selected players
if selected_players:
    player_df = filtered_df[filtered_df['PLAYER_NAME'].isin(selected_players)]
else:
    player_df = filtered_df

# Display filtered data in a table
st.dataframe(player_df)


comparisons = ["Height", "Weight"] # array used for allowing users to choose how ot select their players
#ask users how they would like to compare players
compare_how = st.selectbox("Compare Based Uppon", 
                           comparisons)

if compare_how:
    if compare_how == "Height":
        col1, col2 = st.columns(2)

        with col1:
            fig_height = px.bar(player_df, x='PLAYER_NAME', y='HEIGHT_WO_SHOES', color='PLAYER_NAME',
                                title=f'Player Height (No Shoes) for {year} Season',
                                labels={'HEIGHT_WO_SHOES': 'Height (No Shoes)', 'PLAYER_NAME': 'Player Name'},
                                barmode='group')
            st.plotly_chart(fig_height)

        with col2:
            fig_wingspan = px.bar(player_df, x='PLAYER_NAME', y='WINGSPAN', color='PLAYER_NAME',
                                  title=f'Player Wingspan for {year} Season',
                                  labels={'WINGSPAN': 'Wingspan', 'PLAYER_NAME': 'Player Name'},
                                  barmode='group')
            st.plotly_chart(fig_wingspan)

    elif compare_how == "Weight":
        col1, col2 = st.columns(2)

        with col1:
            fig_weight = px.bar(player_df, x='PLAYER_NAME', y='WEIGHT', color='PLAYER_NAME',
                                title=f'Player Weight for {year} Season',
                                labels={'WEIGHT': 'Weight (lbs)', 'PLAYER_NAME': 'Player Name'},
                                barmode='group')
            st.plotly_chart(fig_weight)

        with col2:
            fig_body_fat = px.bar(player_df, x='PLAYER_NAME', y='BODY_FAT_PCT', color='PLAYER_NAME',
                                  title=f'Player Body Fat % for {year} Season',
                                  labels={'BODY_FAT_PCT': 'Body Fat %', 'PLAYER_NAME': 'Player Name'},
                                  barmode='group')
            st.plotly_chart(fig_body_fat)
        
        # Adding a scatter plot to show the relationship between weight and body fat %
        fig_weight_body_fat = px.scatter(player_df, x='WEIGHT', y='BODY_FAT_PCT', color='PLAYER_NAME',
                                         title=f'Player Weight vs Body Fat % for {year} Season',
                                         labels={'WEIGHT': 'Weight (lbs)', 'BODY_FAT_PCT': 'Body Fat %'})
        st.plotly_chart(fig_weight_body_fat)
        