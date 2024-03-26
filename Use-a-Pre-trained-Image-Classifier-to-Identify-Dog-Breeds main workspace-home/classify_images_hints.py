#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 3" for the classify_images function 
#       Specifically EDIT and ADD code to define the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. The classifier
    labels are formatted to match the pet image labels by converting them to lowercase
    and stripping leading and trailing whitespace.
    
    Parameters:
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                    index 0 = pet image label (string)
                    --- where index 1 & index 2 are added by this function ---
                    NEW - index 1 = classifier label (string)
                    NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                                      and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet, alexnet, vgg (string)
     Returns:
           None - results_dic is a mutable data type so no return needed.         
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
        # Call the classifier function to get the classifier label
        model_label = classifier(images_dir + key, model)
        
        # Format the classifier label
        model_label = model_label.lower().strip()
        
        # Get the pet label from the results dictionary
        truth = results_dic[key][0]
        
        # Check if the pet label is in the classifier label
        if truth in model_label:
            # If there's a match, set the match value to 1
            results_dic[key].extend([model_label, 1])
        else:
            # If there's no match, set the match value to 0
            results_dic[key].extend([model_label, 0])


