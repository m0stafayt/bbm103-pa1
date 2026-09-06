# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

from typing import Any


CART : dict ={} # Define your cart structure here. It should be a dictionary.

SPECIAL_OFFER_ITEMS = {"coffee" , "apple" , "cereal" , "cheese" , "pasta"} # Define your special offer items here. It should be a set or list.

COUPON_CODES: dict ={"WELCOME10" : 0.10 , "SAVE20" : 0.20 , "MEGA25" : 0.25}  # Define your coupon codes here. It should be a dictionary containing coupon codes as keys and their discount percentages (like 0.10 for 10%) as values.

USED_COUPONS = set() # Define your used coupons here. It should be a set or list.

# YOU CAN ALSO DEFINE ADDITIONAL VARIABLES IF NEEDED.


def add_item_to_cart(item_name : str, quantity: int, unit_price: float) -> None:
    """
    Add an item to the shopping cart.

    Arguments:
        item_name (str): The name of the item to add.
        quantity (int): The quantity of the item to add.
        unit_price (float): The unit price of the item.

    Reminder:
        Do NOT print anything.

    Returns:
        None
    """
    # Your implementation here

    #Control for invalid inputs.
    if quantity>0 and unit_price>0:
        if item_name in CART:
            CART[item_name][0]+=quantity
        else:
            CART[item_name]=[quantity,unit_price]
    


def remove_item_from_cart(item_name: str, quantity: int) -> None:
    """
    Remove an item from the shopping cart.

    Arguments:
        item_name (str): The name of the item to remove.
        quantity (int): The quantity of the item to remove.

    Returns:
        None
    """
    # Your implementation here
    if item_name in CART and quantity>0:
        #If removal quantity is greater than or equal to current quantity remove the item completely from the CART.
        if quantity>=CART[item_name][0]:
            CART.pop(item_name)
        else:
            CART[item_name][0]-=quantity


def display_cart() -> str:
    """
    Display the contents of the shopping cart.

    Arguments:
        None

    TODO:
        1. If the cart is empty, RETURN the string "Your cart is empty."
        2. Otherwise, return a multi-line string listing all items and their details. If an item is in SPECIAL_OFFER_ITEMS,
        append a star (*) next to its name.
        Example format:
            Item: apple | Quantity: 2 | Unit price: 10.00
            Item: milk * | Quantity: 1 | Unit price: 25.00

    Reminder:
        - Do NOT print anything. Only return the string.
        - Do NOT modify the cart.

    Returns:
        str: A multi-line string representation of the cart contents or a message indicating the cart is empty.
    """
    
    # Your implementation here

    #If nothing is added to the cart, it will return empty.
    if CART=={}:
        return "Your cart is empty."
    else:
        #Build a multi line string
        all_items=""
        for item in CART:
            if item in SPECIAL_OFFER_ITEMS:
                all_items += (f"Item: {item} * | Quantity: {CART[item][0]} | Unit price: {CART[item][1]:.2f}\n")
            else:
                all_items += (f"Item: {item} | Quantity: {CART[item][0]} | Unit price: {CART[item][1]:.2f}\n")
        return all_items

def get_cart_summary() -> str:
    """
    Get a summary of the shopping cart.

    Arguments:
        None

    Example format:
        Total Items: 7
        Total Quantity: 10
        Total price before discount: 155.00
        Special Offer Items: 2

    Reminder:
        - Do NOT print anything. Only return the string.
        - Do NOT modify the cart.
    
    Returns:
        str: A multi-line string representation of the cart summary.
    """
    # Your implementation here
    items_total_quantity=0
    total_price=0
    special_items=0
    #Calculate summary statictics in a single loop.
    for item in CART:
        items_total_quantity+=CART[item][0]
        total_price+=CART[item][0]*CART[item][1]
        if item in SPECIAL_OFFER_ITEMS:
            special_items+=1

    summary_string = (f"Total Items: {len(CART)}\n"
                    f"Total Quantity: {items_total_quantity}\n"
                    f"Total price before discount: {total_price:.2f}\n"
                    f"Special Offer Items: {special_items}")
    
    return summary_string


def calculate_total_price(coupon_code: str) -> float:
    """
    Calculates the final total cost of the cart, applying all discounts.

    Arguments:
        coupon_code (str): A coupon code that may provide an additional discount to the total cart value.

    IMPORTANT:
        - Discounts are additive for quantity and special offer items.
        - Coupon codes apply to the total cart value after item-level discounts.
        - Round the final total price to 2 decimal places.
    Returns:
        float: The final total cost of the cart after applying all discounts.    
    """
    # Your implementation here
    total_price=0
    for item in CART:
        total_discount=0
        #10% bulk discount for quantity > 3
        if CART[item][0]>3:
            total_discount+=0.10
        #5% special offer discount for eligible items
        if item in SPECIAL_OFFER_ITEMS:
            total_discount+=0.05
        total_price+=((CART[item][0]*CART[item][1])*(1-total_discount)) 
    # Apply coupon discount only if it is valid and unused
    if coupon_code in COUPON_CODES and coupon_code not in USED_COUPONS:
        total_price= total_price*(1-COUPON_CODES[coupon_code])
        USED_COUPONS.add(coupon_code)
    return round(total_price , 2)





class ShoppingCartWindow(QWidget):
    """
    You do NOT need to modify this class.
    It uses the functions you implement above to interact with the cart.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Smart Shopping Cart System')
        self.setGeometry(600, 200, 600, 500)
        self.initUI()
        self.applystyles()

    def applystyles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f7f9fc;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QGroupBox {
                background-color: #ffffff;
                border: 1px solid #dbe3eb;
                border-radius: 8px;
                margin-top: 10px;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 5px 10px;
                background-color: #eaf1f8;
                border-radius: 5px;
                color: #2c3e50;
                font-weight: bold;
            }
            QLabel {
                color: #34495e;
            }
            QLineEdit {
                border: 1px solid #bdc3c7;
                padding: 8px;
                border-radius: 5px;
                background-color: #ffffff;
            }
            QTextEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                background-color: #ffffff;
                color: #2c3e50;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                font-weight: bold;
                border: none;
                padding: 10px 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            #StatusLabel {
                color: #7f8c8d;
                font-style: italic;
            }
        """)
    
    def initUI(self):
        # main layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(15)
        self.main_layout.setContentsMargins(15, 15, 15, 15)

        # --- Title ---
        self.title_label = QLabel("Welcome to the Smart Cart")
        self.title_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # --- Item Management Group ---
        self.item_group = QGroupBox("Manage Items")
        self.item_layout = QFormLayout()
        
        self.item_name_input = QLineEdit()
        self.item_name_input.setPlaceholderText("e.g., apple")
        self.item_layout.addRow("Item Name:", self.item_name_input)
        
        self.quantity_input = QLineEdit()
        self.quantity_input.setPlaceholderText("e.g., 2")
        self.item_layout.addRow("Quantity:", self.quantity_input)

        self.unit_price_input = QLineEdit()
        self.unit_price_input.setPlaceholderText("e.g., 10.0")
        self.item_layout.addRow("Unit Price:", self.unit_price_input)
        
        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add to Cart")
        self.add_button.clicked.connect(self.handle_add_item)
        self.remove_button = QPushButton("Remove from Cart")
        self.remove_button.clicked.connect(self.handle_remove_item)
        self.remove_button.setStyleSheet("QPushButton { background-color: #e74c3c; } QPushButton:hover { background-color: #c0392b; }")

        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.remove_button)
        
        self.item_layout.addRow(self.button_layout)
        self.item_group.setLayout(self.item_layout)
        self.main_layout.addWidget(self.item_group)


        # --- Cart Display and Summary Group ---
        self.cart_group = QGroupBox("Shopping Cart")
        self.cart_layout = QVBoxLayout()

        display_btn = QPushButton("Display Cart Contents")
        self.cart_text = QTextEdit()
        self.cart_text.setReadOnly(True)
        
        display_btn.clicked.connect(self.handle_display_cart)
        display_btn.setStyleSheet("QPushButton { background-color: #9b59b6; } QPushButton:hover { background-color: #8e44ad; }")
        
        self.cart_layout.addWidget(display_btn)
        self.cart_layout.addWidget(self.cart_text)

        summary_btn = QPushButton("Show Cart Summary")
        self.summary_text = QTextEdit()
        self.summary_text.setReadOnly(True)
        summary_btn.clicked.connect(self.handle_summary)
        summary_btn.setStyleSheet("QPushButton { background-color: #f39c12; } QPushButton:hover { background-color: #e67e22; }")

        self.cart_layout.addWidget(summary_btn)
        self.cart_layout.addWidget(self.summary_text)
        
        
        self.cart_group.setLayout(self.cart_layout)
        self.main_layout.addWidget(self.cart_group)

        # --- Total Price Calculation Group ---
        self.total_group = QGroupBox("Calculate Total Price")
        self.total_layout = QVBoxLayout()

        self.coupon_layout = QHBoxLayout()
        self.coupon_input = QLineEdit()
        self.coupon_input.setPlaceholderText("Enter coupon code (e.g., WELCOME10)")
        self.calculate_total_button = QPushButton("Calculate Total")
        self.calculate_total_button.clicked.connect(lambda: self.handle_calculate_total(self.coupon_input.text().strip()))
        self.calculate_total_button.setStyleSheet("QPushButton { background-color: #27ae60; } QPushButton:hover { background-color: #229954; }")

        self.total_display = QLabel("Click 'Calculate Total' to see your summary.")
        self.total_display.setAlignment(Qt.AlignLeft)
        self.total_display.setWordWrap(True)
        self.total_layout.addWidget(self.total_display)

        self.coupon_layout.addWidget(self.coupon_input)
        self.coupon_layout.addWidget(self.calculate_total_button)
        self.total_layout.addLayout(self.coupon_layout)
        self.total_group.setLayout(self.total_layout)
        self.main_layout.addWidget(self.total_group)


        # Set main layout
        self.setLayout(self.main_layout)

    def handle_add_item(self) -> None:
        item_name = self.item_name_input.text().strip().lower()
        quantity = self.quantity_input.text().strip()
        unit_price = self.unit_price_input.text().strip()
        
        for k, v in {"Item Name": item_name, "Quantity": quantity, "Unit Price": unit_price}.items():
            if not v:
                QMessageBox.warning(self, "Input Error", f"{k} cannot be empty.")
                return
        
        if not self.is_int(quantity):
            QMessageBox.warning(self, "Input Error", "Quantity must be a integer.")
            return
        
        if not self.is_float(unit_price):
            QMessageBox.warning(self, "Input Error", "Unit Price must be a number.")
            return
        

        quantity = int(quantity)
        unit_price = float(unit_price)

        add_item_to_cart(item_name, quantity, unit_price)

        # clear text fields
        self.item_name_input.clear()
        self.quantity_input.clear()
        self.unit_price_input.clear()

    
    def handle_remove_item(self) -> None:
        item_name = self.item_name_input.text().strip().lower()
        quantity = self.quantity_input.text().strip()

        for k, v in {"Item Name": item_name, "Quantity": quantity}.items():
            if not v:
                QMessageBox.warning(self, "Input Error", f"{k} cannot be empty.")
                return
        
        if not self.is_int(quantity):
            QMessageBox.warning(self, "Input Error", "Quantity must be a integer.")
            return

        quantity = int(quantity)
        remove_item_from_cart(item_name, quantity)

        # clear text fields
        self.item_name_input.clear()
        self.quantity_input.clear()
        self.unit_price_input.clear()

    
    def handle_display_cart(self) -> None:
        cart_contents = display_cart()
        self.cart_text.setPlainText(cart_contents)

    def handle_summary(self) -> None:
        summary = get_cart_summary()
        self.summary_text.setPlainText(summary)

    def handle_calculate_total(self, coupon_code: str) -> None:
        total_price = calculate_total_price(coupon_code)
        self.total_display.clear()
        self.total_display.setText(f"Total Price: {total_price:.2f}")
        
    
    def is_float(self, value: Any) -> bool:
        if value is None:
            return False
        try:
            float(value)
            return True
        except ValueError:
            return False
    
    def is_int(self, value: Any) -> bool:
        if value is None:
            return False
        try:
            int(value)
            return True
        except ValueError:
            return False
               


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ShoppingCartWindow()
    window.show()
    sys.exit(app.exec_())