# pandas.DataFrame data clustering: cluster data by date (like month, year, etc)

import pandas as pd
import numpy as np

def data_clustering(df : pd.DataFrame) -> pd.DataFrame:
    """
    Data preprocessing.
    """
    # sort by date
    df = df.sort_values(by=['Tarih'])
    # cluster data by date (like month, year, etc)
    df = df.groupby(['Tarih']).sum()
    return df