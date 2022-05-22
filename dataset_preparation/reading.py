import pandas as pd



def read_csv_file_to_pdframe(filepath : str) -> pd.DataFrame:
    """
    Read csv file to pandas dataframe.
    """
    df =  pd.read_csv(filepath, sep=',', header=0, low_memory=False)
    return df
