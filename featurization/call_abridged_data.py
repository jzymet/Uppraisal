import pandas as pd
import numpy as np
from pandas import DataFrame

def read_data() -> DataFrame:
    """
    reads in csv, returning DataFrame
    """

    data = pd.read_csv("abridged_dataset.csv", encoding = 'ISO-8859-1')

    #fill empty values in description with empty string
    data["description"] = data["description"].replace(np.nan, '', regex=True)

    return data