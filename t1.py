"""
Plotting graphs for tournament results in t1: two groups at a time (50/50)
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import pprint
import seaborn as sns

def main():
    path = "/Users/juliannayu/Documents/(24, fall)/coms w4444/Community-Tournament/t1"
    files = os.listdir(path)

    # tasks in 10000 turns for each pairing 
    # task_pairs: dict[distribution_group] = dict[group_number] = dict[other_group_number]: tasks
    task_pairs = {}

    for filename in files:

        split_filename = filename.split("_")
        split_filename[-1] = split_filename[-1][:-4] # taking the .csv out of the last split

        filename = "./t1/" + filename

        if split_filename[1][0] != "m":
            print ("number of members not indicated")
        if split_filename[2][0] != "a":
            print ("number of abilities not indicated")
        if split_filename[3][0] != "g":
            print ("group number not indicated")
        if split_filename[5][0] != "t":
            print ("task difficulty group number not indicated")
        if split_filename[7][0] != "a":
            print ("abilities difficulty group number not indicated")

        num_members = split_filename[1][1:]
        num_abilities = split_filename[2][1:]
        group_num = int(split_filename[3][1:])
        other_group_num = int(split_filename[4])
        task_difficulty_group = split_filename[5][1:]
        task_difficulty = split_filename[6]
        abilities_difficulty_group = split_filename[7][1:]
        abilities_difficulty = split_filename[8]

        df = pd.read_csv(filename)
        # print (str(group_num) + ", " + task_difficulty_group)


        num_tasks = 0

        if df.size > 27:
            num_tasks = df.iloc[9]["Completed Tasks"]
        
        if (task_difficulty_group, task_difficulty) not in task_pairs:
            task_pairs[(task_difficulty_group, task_difficulty)] = {
                1: [0] * 10,
                2: [0] * 10,
                3: [0] * 10,
                4: [0] * 10,
                5: [0] * 10,
                6: [0] * 10,
                7: [0] * 10,
                8: [0] * 10,
                9: [0] * 10,
                10: [0] * 10
            }

        task_pairs[(task_difficulty_group, task_difficulty)][group_num][other_group_num - 1] = num_tasks
        task_pairs[(task_difficulty_group, task_difficulty)][other_group_num][group_num - 1] = num_tasks


        # task_pairs[(task_difficulty_group, task_difficulty)][0].append(group_num)
        # task_pairs[(task_difficulty_group, task_difficulty)][1].append(other_group_num)
        # task_pairs[(task_difficulty_group, task_difficulty)][2].append(num_tasks)
        # task_pairs[(task_difficulty_group, task_difficulty)][0].append(other_group_num)
        # task_pairs[(task_difficulty_group, task_difficulty)][1].append(group_num)
        # task_pairs[(task_difficulty_group, task_difficulty)][2].append(num_tasks)
        
        # if df.size > 27:
        #     num_tasks = df.iloc[9]["Completed Tasks"]

        # task_pairs[(task_difficulty_group, task_difficulty)][group_num][other_group_num] = num_tasks
        # task_pairs[(task_difficulty_group, task_difficulty)][other_group_num][group_num] = num_tasks

    
    for group_distribution in task_pairs:
        distribution = group_distribution[0]
        difficulty = group_distribution[1]
        df1 = pd.DataFrame.from_dict(task_pairs[group_distribution])
        df1.index = np.arange(1, len(df1) + 1)
        print (df1.head)
        sns.heatmap(df1, cmap = 'viridis', annot=True, fmt=".2f", linewidths=.5)
        plt.xlabel("Group")
        plt.ylabel("Other Group")
        plt.title("Tasks Completed in Pairs for Group " + str(distribution) + "'s " + difficulty.capitalize() + " Distributions")
        plt.show()
        # plot_filename = "./t1_plots/" + distribution + ".jpg"
        # plt.savefig(plot_filename, format="jpg")
        







if __name__ == "__main__": 
    main()