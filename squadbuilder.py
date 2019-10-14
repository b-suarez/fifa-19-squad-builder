import pandas as pd
import numpy as np
import aux


class SquadBuilder:
    # Initialize empty Dataframe
    data = pd.DataFrame()

    positionsDictionary = {
        "GK": ["GKDiving", "GKHandling", "GKReflexes"],
        "CB": ["Standing Tackle", "Strenght", "Balance", "Acceleration"]
    }

    def __init__(self, CSVPath):
        """Initializes Squad Builder object given the correct CSV path"""
        self.data = pd.read_csv(CSVPath)

    def get_best_player(self, position, budget="200M"):
        if(position == "GK"):

            goalkeepers_df = self.data.loc[self.data.Position == "GK"]

            for index, row in goalkeepers_df.iterrows():
                avg_key_att = 0.0
                for value in self.positionsDictionary["GK"]:
                    avg_key_att = avg_key_att + float(row[value])

                avg_key_att = (avg_key_att /
                               aux.count_values_dict_key(
                                                      self.positionsDictionary,
                                                      "GK"))
                if(avg_key_att >= 80):
                    print("Average: " + str(avg_key_att))

        return "NULL"

    def _get_float_from_value(value):
        value.replace("M", "")