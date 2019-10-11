import pandas as pd
import numpy as np 

def returnBestKeeper(availablePlayers):
    goodReflexes = fifa19_pd.GKReflexes >=85
    goodPositioning = fifa19_pd.GKPositioning >=85
    return availablePlayers[goodPositioning][goodReflexes]

    
      
    


fifa19_pd = pd.read_csv("datasets/fifa19.csv")


print(returnBestKeeper(fifa19_pd))


