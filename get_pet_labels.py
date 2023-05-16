#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Vu Dong Nguyen Huynh
# DATE CREATED: 05/13/2023                                 
# REVISED DATE: 05/15/2023
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from os import path
# Import Regular Expression to process label
import re

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    result = {}
    files = [f for f in listdir(image_dir)]
    for f in files:
        label = ""
        # Skip files staring with "." in filename
        if f[0] != ".":
            # Format the files name: convert to lower case, replace "_" and "-" with space
            # and remove the file format
            label = f.lower().replace("_"," ").replace("-"," ").split(".")[0]
            # remove multiple spaces if found in file name
            label = re.sub(" +"," ", label)
            # Strip trailling spaces
            label = label.strip()
        
        # Investigate each character in the label, cut the label if any non-letter detected
        for i in range(len(label)):
            if not label[i].isalpha() and label[i] != " ":
                label = label[0:i]
                label = label.strip()
                break
        # Add label as value with name as file name into result dictionary
        result[f] = [label]
        
    # if already exists in Result Dictionary and display warning to user,
    # still need to add into dictionary after warning
    # because different filenames may end up with same label after label processing
    #  --e.g chihuahua3.jpg and chihuahua-19.jpg will end up with same Label after processing
    # (Filename duplication in folder will never happen so need not to check for)


    # Create temporary dictionary to store duplicated values
    duplicated = {}
    
    for key, values in result.items():
        # since Label will be stored in Result Dictionary as List with index = 0
        # check for duplication on this index
        temp = values[0]
        # For this duplicated Dictionary, keys will be duplicated values in Result Dictionary
        # and value will be list of keys of the Result Dictionary (filenames)
        if temp not in duplicated:
            duplicated[temp] = [key]
        else:
            duplicated[temp].append(key)

    for key, value in duplicated.items():
         # Display warning if more than 1 Filename result in single Label
        if len(value) > 1:
            message = "Found duplicated label \'{}\' in {} files :{}"
            print(message.format(key, len(value), value))
   
    return result
