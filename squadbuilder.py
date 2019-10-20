import pandas as pd
import numpy as np
import aux
import matplotlib.pyplot as plt


class SquadBuilder:
    # Initialize empty Dataframe
    data = pd.DataFrame()

    positions_dict = {
        "GK": ["gkdiving", "gkhandling", "gkreflexes"],
        "CB": ["standingtackle", "strength", "balance", "acceleration",
               "interceptions", "marking"],
        "RB": ["stamina", "marking", "slidingtackle", "acceleration",
               "sprintspeed", "crossing"],
        "LB": ["stamina", "marking", "slidingtackle", "acceleration",
               "sprintspeed", "crossing"],
        "CM": ["ballcontrol", "balance", "positioning", "vision",
               "shortpassing", "longshots"],
        "CDM": ["ballcontrol", "balance", "positioning", "strength",
                "longpassing", "marking", "standingtackle"],
        "RW": ["sprintspeed", "dribbling", "acceleration", "agility",
               "ballcontrol", "crossing", "finishing"],
        "LW": ["sprintspeed", "dribbling", "acceleration", "agility",
               "ballcontrol", "crossing", "finishing"],
        "ST": ["finishing", "headingaccuracy", "volleys", "acceleration",
               "shotpower", "jumping", "ballcontrol", "sprintspeed"]
    }

    def __init__(self, CSVPath):
        """Initializes Squad Builder object given the correct CSV path"""
        self.data = pd.read_csv(CSVPath)

        # Set column names as lowercase without spaces
        self.data.columns = map(str.lower, self.data.columns)
        self.data.columns = self.data.columns.str.replace(' ', '')

        # Remove unnamed column
        self.data = self.data.loc[:, ~
                                  self.data.columns.str.contains('^unnamed')]

        # Convert value column to float64
        self.data["value"] = self.data["value"].apply(
            self.__get_float_from_value)

        # Add missingreleaseclause column
        self.data["missingreleaseclause"] = (
            self.data["releaseclause"].isnull()
        )

    def get_best_deals(self):
        df_release_clauses = self.data.dropna(subset=["releaseclause"])

        df_release_clauses["releaseclause"] = (
            df_release_clauses["releaseclause"].apply(
                self.__get_float_from_value
            )
        )

        for index, value in df_release_clauses.iterrows():
            if value['value'] < self.__get_float_from_value(
                    value['release_clause']
            ):
                print(value['name'] + "is valued in " + str(value['value']) +
                      "M but his release clause is " +
                      str(value['release clause']))

    def get_best_player(self, position, budget="300"):
        """Given a player position and a budget, returns a dictionary with
        the best available player"""

        if position:
            player_df = self.data.loc[self.data.position == position]
            best_player_available = dict()
            best_avg_att = 0.0

            for index, row in player_df.iterrows():
                avg_key_att = 0.0

                if row["value"] <= budget:
                    for value in self.positions_dict[position]:
                        avg_key_att = avg_key_att + float(row[value])

                    avg_key_att = (avg_key_att /
                                   aux.count_values_dict_keys(
                                       self.positions_dict, position))

                    if avg_key_att >= best_avg_att:
                        best_avg_att = avg_key_att
                        best_player_available = row

        return best_player_available

    def __get_float_from_value(self, value):
        """Giving a string with format
        "/€/d{x}/M" returns the value as a float"""
        if "K" in value:
            str_value = value.replace("K", "").replace("€", "")
            float_value = float(str_value)/1000
        else:
            str_value = value.replace("M", "").replace("€", "")
            float_value = float(str_value)

            return float_value

    def __get_has_release_clause(self, df):
        has_release_clause = []
        for index, row in df.iterrows():
            if(row['Release Clause'] != 'NaN'):
                has_release_clause.append('1')

            else:
                has_release_clause.append('0')
                print('DASIDNSAUIDBNIAS')

        return has_release_clause
