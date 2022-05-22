# pandas.DataFrame data preprocessing : data cleaning and data reduction such as:
# remove null columns, 
# remove null rows,
# inconsistent data,
# remove empty columns,

import pandas as pd
import numpy as np

def data_preprocessing(df : pd.DataFrame, DATANAME : str) -> pd.DataFrame:
    """
    Data preprocessing.
    """
    df = df.drop_duplicates()

    """"
    # remove null and empty strings
    df = df.dropna()
    # remove inconsistent data and remove duplicates
    df = df.drop_duplicates()
    """

    return df


