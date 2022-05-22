# Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fitting Random Forest Regression to the dataset
from sklearn.ensemble import RandomForestRegressor
 

def random_forest_prediction(sales_for_specific_product : pd.DataFrame) -> int:
    """
    Random Forest prediction.
    """
    # get product sales infos (only transaction_at and price)
    if(len(sales_for_specific_product) == 0):
        return 0
    
    # change every  string sales_for_specific_product['BFIYAT'] to float e.g. 5,00 to 5.0
    sales_for_specific_product['BFIYAT'] = sales_for_specific_product['BFIYAT'].str.replace(',', '.').astype(float)

     # create regressor object
    regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)

    # index[3] URUNREF
    # index[0] LOGICALREF

    x_logical_ref= sales_for_specific_product.iloc[:,0:]
    y_price = sales_for_specific_product.iloc [:,3:]

    # fit the regressor with x and y data
    regressor.fit(x_logical_ref, y_price) 


    predicted_price = regressor.predict(np.array([6.5]).reshape(1, 1)) 
    # return predicted price
    return predicted_price
