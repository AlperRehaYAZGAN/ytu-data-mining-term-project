# price_prediction is the algorithm function file that is used for 
# predict product price by linear regression.


import pandas as pd
import numpy as np


def predict_basket_new_item(sales : pd.DataFrame, intent_products : pd.DataFrame, algorithm = "LINEAR_REGRESSION") -> pd.DataFrame:
    """
    Predict new basket elements from current ones.
    """
    # search products sales infos in sales table foreach product in intent_products

