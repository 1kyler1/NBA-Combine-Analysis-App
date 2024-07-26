from nba_api.stats.static import players
from nba_api.stats.endpoints import draftcombineplayeranthro
import pandas as pd
# import requests
# import numpy as np



# season ids for year stored in a dictionary for fast access
season_id = {2020: "2020", 2021: "2021", 2022: "2022", 2023: "2023", 2024: "2024"}



# gets the player combine stats for each year
def player_combine_stats_year(season_year_id):

    # gets player anthro stats based uppon the year and sorts it in variable year_stats
    year_stats = draftcombineplayeranthro.DraftCombinePlayerAnthro(league_id='00', season_year=season_year_id)
    df = year_stats.get_data_frames()[0] # uses pandas to get a dats frame for the year stats
    df['SEASON_YEAR'] = season_year_id
    return df

# creates a pandas data frame for all the seasons in season_id dictionary
all_seasons_df = pd.DataFrame()

for season in season_id.values():
    season_df = player_combine_stats_year(season)
    all_seasons_df = pd.concat([all_seasons_df, season_df], ignore_index=True)

# creates a csv file with all the seasons and information to insure fast and eficient information lookup
all_seasons_df.to_csv('player_combine_stats.csv', index=False)


    





















