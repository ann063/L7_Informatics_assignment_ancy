#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:23:14 2024

@author: ancysharmila
"""

import sqlite3

# Function to add a new flavor to the database
def add_seasonal_flavor(flavor_name, available_season):
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (flavor_name, available_season) VALUES (?, ?)", (flavor_name, available_season))
    connection.commit()
    connection.close()

# Function to add a new ingredient to the inventory
def add_ingredient(ingredient_name, stock_quantity):
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO ingredient_inventory (ingredient_name, stock_quantity) VALUES (?, ?)", (ingredient_name, stock_quantity))
    connection.commit()
    connection.close()

# Function to add a new customer flavor suggestion
def add_customer_suggestion(suggested_flavor):
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customer_suggestions (suggested_flavor) VALUES (?)", (suggested_flavor,))
    connection.commit()
    connection.close()

# Function to add a new allergen to the database
def add_allergen(allergen_name):
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO allergens (allergen_name) VALUES (?)", (allergen_name,))
    connection.commit()
    connection.close()

# Function to add a flavor to the customer cart
def add_flavor_to_cart(flavor_id):
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customer_cart (flavor_id) VALUES (?)", (flavor_id,))
    connection.commit()
    connection.close()

# Function to search for flavors by season
def search_seasonal_flavors(season=None):
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    if season:
        cursor.execute("SELECT * FROM seasonal_flavors WHERE available_season=?", (season,))
    else:
        cursor.execute("SELECT * FROM seasonal_flavors")
    results = cursor.fetchall()
    connection.close()
    return results

# Function to list items in the customer cart
def view_customer_cart():
    connection = sqlite3.connect('ice_cream_shop.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer_cart")
    results = cursor.fetchall()
    connection.close()
    return results

if __name__ == "__main__":
    while True:
        print("\nIce Cream Shop Menu")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Flavor Suggestion")
        print("4. Add Allergen")
        print("5. Add Flavor to Cart")
        print("6. Search Seasonal Flavors")
        print("7. View Cart")
        print("8. Exit")
        user_choice = input("Choose an option: ")

        if user_choice == '1':
            flavor_name = input("Enter flavor name: ")
            available_season = input("Enter available season: ")
            add_seasonal_flavor(flavor_name, available_season)
        elif user_choice == '2':
            ingredient_name = input("Enter ingredient name: ")
            stock_quantity = int(input("Enter quantity: "))
            add_ingredient(ingredient_name, stock_quantity)
        elif user_choice == '3':
            suggested_flavor = input("Enter flavor suggestion: ")
            add_customer_suggestion(suggested_flavor)
        elif user_choice == '4':
            allergen_name = input("Enter allergen: ")
            add_allergen(allergen_name)
        elif user_choice == '5':
            flavor_id = int(input("Enter flavor ID to add to cart: "))
            add_flavor_to_cart(flavor_id)
        elif user_choice == '6':
            season = input("Enter season to filter by (leave blank for all): ")
            flavors = search_seasonal_flavors(season)
            for flavor in flavors:
                print(flavor)
        elif user_choice == '7':
            cart_items = view_customer_cart()
            for item in cart_items:
                print(item)
        elif user_choice == '8':
            break
        else:
            print("Invalid option, please try again.")