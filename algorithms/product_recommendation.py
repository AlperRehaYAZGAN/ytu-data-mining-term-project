# price_prediction is the algorithm function file that is used for 
# predict product price by linear regression.


import pandas as pd
import numpy as np


def predict_basket_new_item(sales : pd.DataFrame, product_id : str, algorithm = "LINEAR_REGRESSION") -> pd.DataFrame:
    """
    Predict new basket elements from current ones.
    """
    # search products sales infos in sales table foreach product in intent_products
    # sales is pandas dataframe table.
    print("Predicting basket new item...")

    # do operation on sales table
    # SELECT agg_string(sales.URUNREF) FROM sales GROUP BY sales.FISNO WHERE product_id IN intent_products
    sales = sales.groupby(["FISNO"]).agg({"URUNREF": lambda x: ",".join(str(x))})
    print("Predicting basket new item...")

    # find all sales containing intent_products[]

    print(sales)

