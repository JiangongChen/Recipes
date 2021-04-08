# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:50:15 2021

@author: chenj
"""

import numpy as np
from datetime import date

RECIPE_NUM = 13
RECIPE_LIST_NAME = 'recipes_list_v1.txt'

if __name__ == '__main__':
    all_recipes = []
    # read all recipes from the file that stores the list
    with open(RECIPE_LIST_NAME) as f:
        lines = f.readlines()
        for line in lines:
            # extrace recipes from the line by deleting the list number 
            tokens = line.split()
            all_recipes.append(' '.join(tokens[1:]))
            
    # randomly choose n recipes from the list
    recipes_gene = np.random.choice(all_recipes,size=RECIPE_NUM,replace=False)
    # print(recipes_gene)
    
    # get the date of today to name the file that stores the generated recipes
    today = date.today()
    day_gene = today.strftime("%m_%d_%Y")
    # print(day_gene)
    
    # store the recipes in the file
    file_name = day_gene + '.txt'
    dire_name = 'history_recipes/'
    with open(dire_name+file_name,'w') as f:
        for i in range(len(recipes_gene)):
            recipe = recipes_gene[i]
            f.write(str(i+1) + '. ' + recipe+'\n')