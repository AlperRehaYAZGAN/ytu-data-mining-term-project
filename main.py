import os
import time

from pandas import DataFrame
from algorithms.price_prediction import predict_product_price
from dataset_preparation.clustering import data_clustering
from dataset_preparation.preprocessing import data_preprocessing

from gui import generate_gui
from dataset_preparation.reading import read_csv_file_to_pdframe 

DATA_KASAHAREKET = "KASAHAREKET.csv"
DATA_MUSTERIHAREKET = "MUSTERIHAREKET.csv"
DATA_SATISFISLERI = "SATISFISLERI.csv"
DATA_URUNHAREKET = "URUNHAREKET.csv"
DATA_URUNLER = "URUNLER.csv"


def main():
    print("Application started.")
    # get process working directory and data folder
    working_dir = os.getcwd()
    data_dir = os.path.join(working_dir, 'data')
    """

    # read datas from csv files using pandas then assign into variables
    print("Reading data from csv files...")
    content_sales_df = read_csv_file_to_pdframe(os.path.join(data_dir, DATA_URUNHAREKET))
    content_products_df = read_csv_file_to_pdframe(os.path.join(data_dir, DATA_URUNLER))
    print("Data reading completed.")

    # (all datas are pandas tables)
    # 1 - data-preparation -- data preprocessing : data cleaning and data reduction such as:
    # --- remove null and empty strings
    # --- remove inconsistent data and remove duplicates 
    # --- sort by date 
    print("Data preprocessing...")
    pre_content_sales_df = data_preprocessing(content_sales_df,"SATISLAR")
    pre_content_products_df = data_preprocessing(content_products_df,"URUNLER")
    print("Data preprocessing completed.")

    # 3 - data-preparation -- data clustering: cluster data by date (like month, year, etc)
    # print("Data clustering...")
    # content_products = data_clustering(content_products)
    # content_sales = data_clustering(content_sales)
    # print("Data clustering completed.")

    # 4 - algorithms -- predict product price
    print("Predicting product price...")
    random_products = pre_content_products_df.iloc[38:47]
    random_products = DataFrame(random_products)
    print("\n\n")
    content_predicted = predict_product_price(pre_content_sales_df,random_products)
    print("Predicting product price completed.")

    # 5 - algorithms -- generate knn model to predict product basket recommendation.
    """


    # 6 - gui -- generate gui
    generate_gui(
        [["","",""],["","",""]],
        [["","",""],["","",""]],
        [["","",""],["","",""]]
    )

# if main 
if __name__ == '__main__':
    # start main and try catch
    try:
        main()
    except Exception as e:
        print("Error: {}".format(e))
        exit(1)
    finally:
        print("Done")
        exit(0)
