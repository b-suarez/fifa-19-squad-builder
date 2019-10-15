import pandas as pd
import numpy as np
import squadbuilder as sqb

builder = sqb.SquadBuilder("datasets/fifa19.csv")
builder.get_best_player("CB", 30)


# def returnBestKeeper(availablePlayers):
#     goodReflexes = fifa19_pd.GKReflexes >=85
#     goodPositioning = fifa19_pd.GKPositioning >=85
#     return availablePlayers[goodPositioning][goodReflexes]
# print(str(fifa19_pd.Name[fifa19_pd.GKPositioning ==
# fifa19_pd.GKPositioning.max()]))
