import pandas as pd
import numpy as np
import aux
import matplotlib.pyplot as plt


class SquadBuilder:
    # Initialize empty Dataframe
    data = pd.DataFrame()

    positions_dict = {
        "GK": ["GKDiving", "GKHandling", "GKReflexes"],
        "CB": ["StandingTackle", "Strength", "Balance", "Acceleration"]
    }

    def __init__(self, CSVPath):
        """Initializes Squad Builder object given the correct CSV path"""
        self.data = pd.read_csv(CSVPath)

        self.data["Value"] = self.data["Value"].apply(
            self.__get_float_from_value)

        # print(self.data['Release Clause'])

        # self.data["Release Clause"] = self.data["Release Clause"].apply(
        #     self.__get_float_from_value)
        # print(self.data.head())

    def get_best_player(self, position, budget="300"):
        """Given a player position and a budget, returns a dictionary with
        the best available player"""

        if position:
            player_df = self.data.loc[self.data.Position == position]
            best_player_available = dict()
            best_avg_att = 0.0

            for index, row in player_df.iterrows():
                avg_key_att = 0.0

                if row["Value"] <= budget:
                    for value in self.positions_dict[position]:
                        avg_key_att = avg_key_att + float(row[value])

                    avg_key_att = (avg_key_att /
                                   aux.count_values_dict_keys(
                                       self.positions_dict, position))

                    if avg_key_att >= best_avg_att:
                        best_avg_att = avg_key_att
                        best_player_available = row

        return best_player_available

    # def get_best_deals(dataframe):
    #     for index, row in dataframe:
    #         if dataframe['']

    def __get_float_from_value(self, value):
        """Giving a string with format
        "/€/d{x}/M" returns the value as a float"""
        if value:
            if "K" in value:
                str_value = value.replace("K", "").replace("€", "")
                float_value = float(str_value)/1000
            else:
                str_value = value.replace("M", "").replace("€", "")
                float_value = float(str_value)

            return float_value

        else:
            return 'NaN'
