import pandas as pd
import numpy as np
from pandas import DataFrame

def get_year_mention_features(laptopData: DataFrame) -> DataFrame:
    """
    reads in laptopData DataFrame, returns augmented DataFrame with columns checking for whether laptop manufacture year
    is mentioned in the title and description
    :param laptopData: dataframe
    """

    #instantiate year-related title/description features
    laptopData["year_in_title"] = False
    laptopData["year_in_description"] = False

    # set year-in-title/year-in-description value to true if year is mentioned in title/description
    for i in range(len(laptopData)):

        if str(laptopData.loc[i, "year"])[:4] in laptopData.loc[i, "title"]:
            laptopData.loc[i, "year_in_title"] = True

        #also have to check if there is a description
        if laptopData.loc[i, "description"] and str(laptopData.loc[i, "year"])[:4] in laptopData.loc[i, "description"]:
            laptopData.loc[i, "year_in_description"] = True

    return laptopData

def get_size_mention_features(laptopData: DataFrame) -> DataFrame:
    """
    reads in laptopData DataFrame, returns augmented DataFrame with columns checking for whether laptop size
    is mentioned in the title and description
    :param laptopData: dataframe
    """
    #instantiate year-related title/description features
    laptopData["size_in_title"] = False
    laptopData["size_in_description"] = False

    # set size-in-title/size-in-description value to true if year is mentioned in title/description
    for i in range(len(laptopData)):

        #need various cases to ensure we're matching to mention of size (e.g., 12 inches rather than 20*12* or *12*0GB)
        if ((" "+str(laptopData.loc[i, "size"])[:2]+" " in laptopData.loc[i, "title"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"in" in laptopData.loc[i, "title"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"-in" in laptopData.loc[i, "title"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"." in laptopData.loc[i, "title"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"'" in laptopData.loc[i, "title"])):
            laptopData.loc[i, "size_in_title"] = True

        #also have to check if there is a description
        if (laptopData.loc[i, "description"] and
            (" "+str(laptopData.loc[i, "size"])[:2]+" " in laptopData.loc[i, "description"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"in" in laptopData.loc[i, "description"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"-in" in laptopData.loc[i, "description"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"." in laptopData.loc[i, "description"]) or
            (" "+str(laptopData.loc[i, "size"])[:2]+"'" in laptopData.loc[i, "description"])):
            laptopData.loc[i, "size_in_description"] = True

    return laptopData

def get_memory_mention_features(laptopData: DataFrame) -> DataFrame:
    """
    reads in laptopData DataFrame, returns augmented DataFrame with columns checking for whether laptop storage capacity
    is mentioned in the title and description
    :param laptopData: dataframe
    """

    # instantiate year-related title/description features
    laptopData["memory_in_title"] = False
    laptopData["memory_in_description"] = False

    # set memory-in-title/memory-in-description value to true if year is mentioned in title/description
    for i in range(len(laptopData)):

        # need case-insensitive chech of various scenarios to ensure we're matching to mention of memory
        if ((" " + str(laptopData.loc[i, "memory"])[:3] + " " in laptopData.loc[i, "title"].lower()) or
            (" " + str(laptopData.loc[i, "memory"])[:3] + "gb" in laptopData.loc[i, "title"].lower()) or
            (" " + str(laptopData.loc[i, "memory"])[:3] + "ssd" in laptopData.loc[i, "title"].lower()) or
            ("1 tb" in laptopData.loc[i, "title"].lower()) or ("1tb" in laptopData.loc[i, "title"].lower()) or
            ("2 tb" in laptopData.loc[i, "title"].lower()) or ("2tb" in laptopData.loc[i, "title"].lower()) or
            ("4 tb" in laptopData.loc[i, "title"].lower()) or ("4tb" in laptopData.loc[i, "title"].lower())):
            laptopData.loc[i, "memory_in_title"] = True

        # also have to check if there is a description
        if (laptopData.loc[i, "description"] and
            (" " + str(laptopData.loc[i, "memory"])[:3] + " " in laptopData.loc[i, "description"].lower()) or
            (" " + str(laptopData.loc[i, "memory"])[:3] + "gb" in laptopData.loc[i, "description"].lower()) or
            (" " + str(laptopData.loc[i, "memory"])[:3] + "ssd" in laptopData.loc[i, "description"].lower()) or
            ("1 tb" in laptopData.loc[i, "description"].lower()) or ("1tb" in laptopData.loc[i, "description"].lower()) or
            ("2 tb" in laptopData.loc[i, "description"].lower()) or ("2tb" in laptopData.loc[i, "description"].lower()) or
            ("4 tb" in laptopData.loc[i, "description"].lower()) or ("4tb" in laptopData.loc[i, "description"].lower())):
            laptopData.loc[i, "memory_in_description"] = True

    return laptopData

def get_adjective_mention_features(laptopData: DataFrame) -> DataFrame:
    """
    reads in laptopData DataFrame, returns augmented DataFrame with columns checking for whether laptop storage capacity
    is mentioned in the title and description
    :param laptopData: dataframe
    """

    # instantiate year-related title/description features
    laptopData["brand_new_in_title"] = False
    laptopData["brand_new_in_description"] = False
    laptopData["new_in_title"] = False
    laptopData["new_in_description"] = False
    laptopData["positive_adjectives_in_title"] = False
    laptopData["positive_adjectives_in_description"] = False
    laptopData["good_in_title"] = False
    laptopData["good_in_description"] = False
    laptopData["used_in_title"] = False
    laptopData["used_in_description"] = False

    # set memory-in-title/memory-in-description value to true if year is mentioned in title/description
    for i in range(len(laptopData)):

        # case-insensitive check for various adjectives in title
        if "brand new" in laptopData.loc[i, "title"].lower():
            laptopData.loc[i, "brand_new_in_title"] = True
        if "new" in laptopData.loc[i, "title"].lower() and not("brand new" in laptopData.loc[i, "title"].lower()):
            laptopData.loc[i, "new_in_title"] = True
        if ("mint" in laptopData.loc[i, "title"].lower()) or ("excellent condition" in laptopData.loc[i, "title"].lower()) or ("great condition" in laptopData.loc[i, "title"].lower()):
            laptopData.loc[i, "positive_adjectives_in_title"] = True
        if "good condition" in laptopData.loc[i, "title"].lower():
            laptopData.loc[i, "good_in_title"] = True
        if "used" in laptopData.loc[i, "title"].lower():
            laptopData.loc[i, "used_in_title"] = True

        # also have to check if there is a description
        if laptopData.loc[i, "description"]:
            if "brand new" in laptopData.loc[i, "description"].lower():
                laptopData.loc[i, "brand_new_in_description"] = True
            if "new" in laptopData.loc[i, "description"].lower() and not ("brand new" in laptopData.loc[i, "description"].lower()):
                laptopData.loc[i, "new_in_description"] = True
            if (("mint" in laptopData.loc[i, "description"].lower()) or
                    ("excellent condition" in laptopData.loc[i, "description"].lower()) or
                    ("great condition" in laptopData.loc[i, "description"].lower())):
                laptopData.loc[i, "positive_adjectives_in_description"] = True
            if "good condition" in laptopData.loc[i, "description"].lower():
                laptopData.loc[i, "good_in_description"] = True
            if "used" in laptopData.loc[i, "description"].lower():
                laptopData.loc[i, "used_in_description"] = True

    return laptopData

def get_length_features(laptopData: DataFrame) -> DataFrame:
    """
    reads in laptopData DataFrame, returns augmented DataFrame with columns checking for whether laptop storage capacity
    is mentioned in the title and description
    :param laptopData: dataframe
    """

    # instantiate year-related title/description features
    laptopData["n_words_in_title"] = 0
    laptopData["n_words_in_description"] = 0

    # loop through titles/descriptions, counting how many spaces occur in each
    for i in range(len(laptopData)):

        title_count = 0
        description_count = 0

        #count spaces in title, set value to n_words_in_title
        for character in laptopData.loc[i, "title"]:
            if character == " ":
                title_count += 1
        laptopData.loc[i, "n_words_in_title"] = title_count

        #count spaces in description, set value to n_words_in_description
        for character in laptopData.loc[i, "description"]:
            if character == " ":
                description_count += 1
        laptopData.loc[i, "n_words_in_description"] = description_count

    return laptopData
