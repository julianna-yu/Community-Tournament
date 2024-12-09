"""
Plotting graphs for tournament results in t4: all groups at once
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pprint

def main():
    path = "/Users/juliannayu/Documents/(24, fall)/coms w4444/Community-Tournament/t4"
    files = os.listdir(path)

    # column names
    turns = "Turn"
    tasks = "Completed Tasks"
    tasks_per_turn = "Tasks/Turn"

    # tasks in 10000 turns
    tasks_per_group = {}

    for filename in files:

        split_filename = filename.split("_")
        split_filename[-1] = split_filename[-1][:-4] # taking the .csv out of the last split

        filename = "./t4/" + filename

        if split_filename[1][0] != "m":
            print ("number of members not indicated")
        if split_filename[2][0] != "a":
            print ("number of abilities not indicated")
        if split_filename[3][0] != "t":
            print ("task difficulty group number not indicated")
        if split_filename[5][0] != "a":
            print ("abilities difficulty group number not indicated")

        num_members = split_filename[1][1:]
        num_abilities = split_filename[2][1:]
        task_difficulty_group = split_filename[3][1:]
        task_difficulty = split_filename[4]
        abilities_difficulty_group = split_filename[5][1:]
        abilities_difficulty = split_filename[6]

        df = pd.read_csv(filename)

        if df.size == 0:
                continue
        df_plot = df.plot(x=turns, y=tasks_per_turn)
        plt.xlabel("Turns")
        plt.ylabel("Tasks per Turn")
        plt.title("Tasks per Turn for Group " + str(task_difficulty_group) + "'s " + task_difficulty.capitalize() + " Distributions")
        plt.suptitle(num_members + " Members and " + num_abilities + " Abilities", size="small")
        plot_filename = "./t4_plots/m" + num_members + "_a" + num_abilities + "_t" + task_difficulty_group + task_difficulty + "_a" + abilities_difficulty_group + abilities_difficulty + ".jpg"
        plt.savefig(plot_filename)
        
        

if __name__ == "__main__": 
    main()