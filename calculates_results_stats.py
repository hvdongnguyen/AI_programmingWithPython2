#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: VU DONG NGUYEN HUYNH  
# DATE CREATED: 05/14/2023                               
# REVISED DATE: 05/15/2023
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """        
    # Create a Results Statistics Dictionary to return stats  
    results_stats_dic = {}
    # 1. Total images
    results_stats_dic["n_images"] = 0
    # 2 & 3. Number of dog and non-dog images
    results_stats_dic["n_dogs_img"] = 0
    results_stats_dic["n_notdogs_img"] = 0
    # 4. number of matches between pet & classifier labels
    results_stats_dic["n_match"] = 0
    # 5 & 6. number of correctly classified dog/non-dog images
    results_stats_dic["n_correct_dogs"] = 0
    results_stats_dic["n_correct_notdogs"] = 0
    # 7 number of correctly classified dog breeds
    results_stats_dic["n_correct_breed"] = 0
    # 8. percentage of correct matches
    results_stats_dic["pct_match"] = 0.0
    # 9 & 10. percentage of correctly classified dogs/non-dogs
    results_stats_dic["pct_correct_dogs"] = 0.0
    results_stats_dic["pct_correct_notdogs"] = 0.0
    # 11. percentage of correctly classified dog breeds
    results_stats_dic["pct_correct_breed"] = 0.0
    
    #=========================================
    # 1. Total images
    results_stats_dic["n_images"] = len(results_dic)
    for key in results_dic:
        # store Results Dictionary value list into variable for easier coding
        pet_image_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        is_match = results_dic[key][2]
        image_label_is_dog = results_dic[key][3]
        classifier_label_is_dog = results_dic[key][4]
        
        stats = [] 
        if image_label_is_dog == 1:
            #2 Number of dog images
            results_stats_dic["n_dogs_img"] += 1
            if classifier_label_is_dog==1:
                #5 Number of correct dog images
                results_stats_dic["n_correct_dogs"] += 1
                if is_match==1:
                    #7 Number of correctly classified dog breeds
                    results_stats_dic["n_correct_breed"] += 1
        else:
            #3 Number of correct dog images
            results_stats_dic["n_notdogs_img"] += 1
            if classifier_label_is_dog == 0:
                #6 Number of correct non-dog images
                results_stats_dic["n_correct_notdogs"] += 1
                
        if is_match == 1:
            #4 Number of matches between pet & classifier labels
            results_stats_dic["n_match"] += 1
               
     # Make sure there is no divide to zero error
    if (results_stats_dic['n_images'] == 0 ):
        results_stats_dic['pct_match'] ="No image(s) found"
        results_stats_dic['pct_correct_breed'] ="No image(s) found"
    else:
        #8. Percentage match
        results_stats_dic["pct_match"] = (results_stats_dic["n_match"]/results_stats_dic["n_images"])
        #11. Percentage of correct dog-breed
        results_stats_dic['pct_correct_breed'] = round((results_stats_dic['n_correct_breed'] /
                                                   results_stats_dic['n_dogs_img']), 2)
    
    #9. Percentage correct dog
    if (results_stats_dic['n_dogs_img'] == 0 ):
        results_stats_dic['pct_correct_notdogs'] ="No dog images found"
    else:
        results_stats_dic['pct_correct_dogs'] = round((results_stats_dic['n_correct_dogs'] /
                                                   results_stats_dic['n_dogs_img']), 2)
    
    #10. Percentage correct non-dog
    if (results_stats_dic['n_notdogs_img'] == 0 ):
        results_stats_dic['pct_correct_notdogs'] ="No not-dog images found"
    else:
        results_stats_dic['pct_correct_notdogs'] = round((results_stats_dic['n_correct_notdogs'] /
                                                   results_stats_dic['n_notdogs_img']), 2)
    
    
    return results_stats_dic
    

