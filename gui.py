#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt6.QtWidgets import (
    QApplication
    ,QWidget
    ,QLabel
    ,QPushButton
    ,QVBoxLayout
    ,QTableWidget
    ,QTableWidgetItem
)

def table_on_item_selected(item : QTableWidgetItem):
    print(item.row())
    pass


def create_table_with_content(header : list[str] ,content : list[str], on_item_clicked : callable) -> QTableWidget:
    """
    Create table with content.
    """
    table = QTableWidget()
    table.setRowCount(len(content))
    table.setColumnCount(len(content[0]))

    for i in range(0, len(content)):
        for j in range(0, len(content[i])):
            tableElement = QTableWidgetItem(content[i][j])
            table.setItem(i, j, tableElement)
            tableElement
            pass
        pass

    table.itemClicked.connect(on_item_clicked)

    return table


def set_table_header(table : QTableWidget , header : list[str]):
    """
    Set the table header.
    """
    table.setHorizontalHeaderLabels(header)


def set_table_content(table : QTableWidget , content : list[list[str]]):
    """
    Set the table content.
    """
    table.setRowCount(len(content))
    table.setColumnCount(len(content[0]))

    for i in range(0, len(content)):
        for j in range(0, len(content[i])):
            table.setItem(i, j, QTableWidgetItem(content[i][j]))
            pass
        pass
    pass




def generate_gui(content_products : list[list[str]], content_sales : list[list[str]], content_predicted : list[list[str]]):
    """
    Start the GUI content.
    """

    # create gui hello world
    app = QApplication([])
    # detect system os and set Style
    app.setStyle('macos')

    window = QWidget()
    v_layout = QVBoxLayout()

    # set 720 width and 360 height
    window.setFixedSize(960, 480)
    # set window title
    window.setWindowTitle("YTU Data Mining Project - 18011016, 18011020")

    # pyqt searchable_table item 


    # label "Products"
    lbl_products = QLabel("Products")
    # products table (button and table)
    table_products = create_table_with_content(content_products[0], content_products[1:], table_on_item_selected)

    btn_add_to_selected = QPushButton("Add to basket")

        
    btn_remove_from_selected = QPushButton("Remove from basket")

    # label "Basket"
    lbl_sales = QLabel("Basket")
    table_selected = create_table_with_content(content_sales[0], content_sales[1:], table_on_item_selected)

    btn_suggest_me_new_product = QPushButton("Suggest me new product")
    # label "Predicted"
    lbl_predicted = QLabel("Recommended Results:")
    table_prediction_result = create_table_with_content(content_predicted[0], content_predicted[1:], table_on_item_selected)

    # set tables to vertical layout
    v_layout.addWidget(lbl_products)
    v_layout.addWidget(table_products)
    v_layout.addWidget(btn_add_to_selected)
    v_layout.addWidget(btn_remove_from_selected)
    v_layout.addWidget(lbl_sales)
    v_layout.addWidget(table_selected)
    v_layout.addWidget(btn_suggest_me_new_product)
    v_layout.addWidget(lbl_predicted)
    v_layout.addWidget(table_prediction_result)


    window.setLayout(v_layout)
    window.show()

    # start the gui
    app.exec()

    pass
