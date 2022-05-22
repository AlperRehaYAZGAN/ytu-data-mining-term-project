# linear_regression = lambda sales : np.mean(sales['UrunFiyati'])

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



def linear_regression(sales_for_specific_product : pd.DataFrame):
    """
    Linear regression.
    """
    # get product sales infos (only transaction_at and price)
    if(len(sales_for_specific_product) == 0):
        return 0
    
    # change every  string sales_for_specific_product['BFIYAT'] to float e.g. 5,00 to 5.0
    sales_for_specific_product['BFIYAT'] = sales_for_specific_product['BFIYAT'].str.replace(',', '.').astype(float)

    sales_for_specific_product.plot.scatter(x="TARIH", y="BFIYAT", alpha=0.5)

    # get linear regression model
    model = LinearRegression()

    # fit model
    model.fit(sales_for_specific_product['LOGICALREF'].values.reshape(-1, 1), sales_for_specific_product['BFIYAT'].values.reshape(-1, 1))
    # predict price
    predicted_price = model.predict(sales_for_specific_product['LOGICALREF'].values.reshape(-1, 1))


    # return predicted price
    return predicted_price
