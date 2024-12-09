"""
Plotting graphs for tournament results in t3: one group at a time
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pprint

def main():
    path = "/Users/juliannayu/Documents/(24, fall)/coms w4444/Community-Tournament/t3"
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

        filename = "./t3/" + filename

        if split_filename[1][0] != "m":
            print ("number of members not indicated")
        if split_filename[2][0] != "a":
            print ("number of abilities not indicated")
        if split_filename[3][0] != "g":
            print ("group number not indicated")
        if split_filename[4][0] != "t":
            print ("task difficulty group number not indicated")
        if split_filename[6][0] != "a":
            print ("abilities difficulty group number not indicated")

        num_members = split_filename[1][1:]
        num_abilities = split_filename[2][1:]
        group_num = int(split_filename[3][1:])
        task_difficulty_group = split_filename[4][1:]
        task_difficulty = split_filename[5]
        abilities_difficulty_group = split_filename[6][1:]
        abilities_difficulty = split_filename[7]

        df = pd.read_csv(filename)
        # print (str(group_num) + ", " + task_difficulty_group)

        # if the file is one of group 10
        # create a line graph to see if the tasks solved per turn is consistent (x: turns, y: tasks per turn)
        if group_num == 10:
            if df.size == 0:
                continue
            df_plot = df.plot(x=turns, y=tasks_per_turn, legend=False)
            plt.xlabel("Turns")
            plt.ylabel("Tasks per Turn")
            plt.title("Tasks per Turn for Group " + str(task_difficulty_group) + "'s " + task_difficulty.capitalize() + " Distributions")
            
            plot_filename = "./t3_plots/g" + str(group_num) + "_t" + task_difficulty_group + task_difficulty + "_a" + abilities_difficulty_group + abilities_difficulty + ".jpg"
            plt.savefig(plot_filename)
        
        if df.size < 99 * 3: 
            continue
        if task_difficulty_group == abilities_difficulty_group and (task_difficulty_group, task_difficulty) not in tasks_per_group:
            tasks_per_group[(task_difficulty_group, task_difficulty)] = {}
            tasks_per_group[(task_difficulty_group, task_difficulty)][group_num] = df.iloc[99][tasks]
        elif task_difficulty_group == abilities_difficulty_group and (task_difficulty_group, task_difficulty) in tasks_per_group:
            tasks_per_group[(task_difficulty_group, task_difficulty)][group_num] = df.iloc[99][tasks]
    print (tasks_per_group)
    for group_distribution in tasks_per_group:
        df1 = pd.DataFrame.from_dict(tasks_per_group[group_distribution], orient='index', columns=["10000 Turns"])
        distribution = group_distribution[0]
        difficulty = group_distribution[1]
        df1 = df1.sort_index()
        df1.plot.bar(legend=False)
        plt.xlabel("Group")
        plt.ylabel("Tasks Completed in 10000 Turns")
        plt.title("Tasks Completed for Group " + str(distribution) + "'s " + difficulty.capitalize() + " Distributions")
        plot_filename = "./t3_plots/" + distribution + ".jpg"
        plt.savefig(plot_filename)
        






if __name__ == "__main__": 
    main()