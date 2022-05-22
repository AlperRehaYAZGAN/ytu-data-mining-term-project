# price_prediction is the algorithm function file that is used for 
# predict product price by linear regression.
import warnings

from algorithms.price_prediction_random_forest import random_forest_prediction
warnings.simplefilter(action='ignore', category=FutureWarning)


import pandas as pd
import numpy as np

from algorithms.price_prediction_regression import linear_regression
from algorithms.price_prediction_ridge import ridge_regression
from algorithms.price_prediction_svm import svm_prediction


def predict_product_price(sales : pd.DataFrame, intent_products : pd.DataFrame, algorithm = "RANDOM_FOREST") -> pd.DataFrame:
    """
    Predict product price.
    """
    # search product sales info in sales table foreach product in intent_products tos ummarize data
    messages = []
    
    for index, row in intent_products.iterrows():
        # get product logical reference

        # pandas select where logical reference is equal to product logical reference
        sales_for_specific_product = sales[sales['URUNREF'] == row['LOGICALREF']]

        # predict product price
        predicted_price = [[]]
        if algorithm == "LINEAR_REGRESSION":
            # linear regression
            predicted_price = linear_regression(sales_for_specific_product)
        elif algorithm == "RIDGE_REGRESSION":
            # ridge regression
            predicted_price = ridge_regression(sales_for_specific_product)
        elif algorithm == "SVM":
            # support vector machine
            predicted_price = svm_prediction(sales_for_specific_product)
        elif algorithm == "RANDOM_FOREST":
            # support vector machine
            predicted_price = random_forest_prediction(sales_for_specific_product)

        # add predicted price (append is deprecated) use concat
        # get predicted price max value
        predicted_price_max = np.max(predicted_price)
        messages.append(str("Algoritma: " + algorithm + " ürün ismi " + row['URUNACIKLAMASI'] + " Satış Fiyatı: " + row['SFIYAT'] + " Tahmini Fiyat: " + str(predicted_price_max)))

    for message in messages:
        print(message)




