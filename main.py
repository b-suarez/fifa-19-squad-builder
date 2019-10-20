import pandas as pd
import numpy as np
import squadbuilder as sqb
import inquirer

builder = sqb.SquadBuilder("datasets/fifa19.csv")

# Initializes the dictionaries with the questions for the user flow
main_menu = [
    inquirer.List('mode',
                  message="What mode do you want to use?",
                  choices=['Squad Builder',
                           'Get Best Player By Budget',
                           "See overalls distribution"
                           ],
                  ),
]
position = [
    inquirer.List('position',
                  message="What position you need to get?",
                  choices=builder.positions_dict.keys()
                  ),
]

answers = inquirer.prompt(main_menu)

if answers["mode"] == "Get Best Player By Budget":
    answers = inquirer.prompt(position)

    budget = input("What is your budget? (In Million Euros) ")
    best_player_available = builder.get_best_player(
        answers["position"], float(budget))

    print("The best player available by that budget is: ")
    print(best_player_available["name"] + " with a value of: " +
          str(best_player_available["value"]) + "M euros and an overall of: " +
          str(best_player_available["overall"]))

elif answers["mode"] == "See overalls distribution":
    builder.overall_histogram()
