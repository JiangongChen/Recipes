# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 23:50:15 2021

@author: chenj
"""

import numpy as np
from datetime import date
import os
import copy

# total number of recipes to be generated
RECIPE_NUM = 13
# number of recipes which are very easy to cook
LAZY_NUM = 2
LAZY_FILE = 'feel_lazy.txt'
# file name which stores regular recipes
RECIPE_LIST_NAME = 'regular.txt'
# directory that stores special recipes, the number of recipes in each category 
# of special recipe will be at most one, except the lazy recipes
SPEC_RECIPE_DIRE = 'special_recipes/'
# directory that stores the generated recipes
TARGET_DIRE = 'history_recipes/'


if __name__ == '__main__':
    all_recipes = []
    # read all recipes from the regular recipe file 
    with open(RECIPE_LIST_NAME) as f:
        lines = f.readlines()
        for line in lines:
            # To avoid some lines have \n, while some not
            tokens = line.split()
            all_recipes.append(' '.join(tokens[:]))
    
    # read recipes from the special recipe directory and store them in a dictionary
    spec_dict = {}
    if os.path.exists(SPEC_RECIPE_DIRE):
        filenames = os.listdir(SPEC_RECIPE_DIRE)
        for filename in filenames:
            spec_recipes = []
            with open(SPEC_RECIPE_DIRE+filename) as f:
                lines = f.readlines()
                for line in lines:
                    tokens = line.split()
                    spec_recipes.append(' '.join(tokens[:]))
            if filename != LAZY_FILE:
                all_recipes.append(filename)
            spec_dict[filename] = spec_recipes
    
    
    # randomly choose n recipes from the list
    recipes_gene = np.random.choice(all_recipes,size=RECIPE_NUM-LAZY_NUM,replace=False)
    for recipe in recipes_gene.copy():
        if recipe in spec_dict:
            recipes_gene = np.delete(recipes_gene, np.argwhere(recipes_gene == recipe))
            spec_recipe = np.random.choice(spec_dict[recipe],size=1,replace=False)
            recipes_gene = np.append(recipes_gene,spec_recipe)
            print('add special recipe: ',spec_recipe[0])
    # add two lazy recipes
    lazy_recipes = np.random.choice(spec_dict[LAZY_FILE],size=LAZY_NUM,replace=False)
    recipes_gene = np.append(recipes_gene,lazy_recipes)
    print('lazy recipes: ',lazy_recipes)
    
    print(recipes_gene)
    
    # get the date of today to name the file that stores the generated recipes
    today = date.today()
    day_gene = today.strftime("%m_%d_%Y")
    # print(day_gene)
    
    # store the recipes in the file
    file_name = day_gene + '.txt'
    with open(TARGET_DIRE+file_name,'w') as f:
        for i in range(len(recipes_gene)):
            recipe = recipes_gene[i]
            f.write(str(i+1) + '. ' + recipe + '\n')