#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:21:14 2024

@author: ancysharmila
"""

import sqlite3

def create_database():
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()

    # Create table for seasonal flavors
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                    id INTEGER PRIMARY KEY,
                    flavor_name TEXT NOT NULL,
                    available_season TEXT NOT NULL
                )''')

    # Create table for ingredient inventory
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                    id INTEGER PRIMARY KEY,
                    ingredient_name TEXT NOT NULL,
                    stock_quantity INTEGER NOT NULL
                )''')

    # Create table for customer flavor suggestions
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                    id INTEGER PRIMARY KEY,
                    suggested_flavor TEXT NOT NULL
                )''')

    # Create table for allergens
    cursor.execute('''CREATE TABLE IF NOT EXISTS allergens (
                    id INTEGER PRIMARY KEY,
                    allergen_name TEXT NOT NULL
                )''')

    # Create table for customer cart
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_cart (
                    id INTEGER PRIMARY KEY,
                    flavor_id INTEGER,
                    FOREIGN KEY (flavor_id) REFERENCES seasonal_flavors (id)
                )''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()
    print("Database and tables created successfully.")